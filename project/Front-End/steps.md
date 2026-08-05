# Connecting the Tailwind Customer Page to the CustomerApp Flask Backend

This is the full, step-by-step build: taking your static Tailwind `customers.html` and wiring it — one capability at a time — to the real Flask + MySQL backend from `CUSTOMERAPP-SETUP.md`. Every step below is real, runnable code, verified end-to-end against a live Flask + MySQL server.

**Build order:** Setup → load & render the table → capture form data (console only) → send data to the backend (Create) → Edit/Update → Delete.

---

## Step 0 — Project Setup

### Folder structure

This guide uses a structure built to scale past just "customers" — `styles/` and `scripts/` at the top level, with `scripts/` split by concern (`api/`, `render/`, `pages/`) and one file per resource inside each. Steps 1–5 below build the `customers` slice; the final section adds a second resource (`orders`) to show the pattern in action with more than one feature.

```
dom-flask-tailwind/
├── customers.html          ← Customer Management page
├── orders.html               ← Orders page (added at the end of this guide)
│
├── styles/
│   ├── base.css              ← shared across every page
│   ├── customers.css          ← customers-page-specific overrides
│   └── orders.css              ← orders-page-specific overrides
│
└── scripts/
    ├── api/
    │   ├── client.js          ← shared BASE_URL + fetch wrapper + error handling
    │   ├── customers.js        ← getCustomers, createCustomer, updateCustomer, deleteCustomer
    │   └── orders.js            ← getOrders, createOrder
    │
    ├── render/
    │   ├── customers.js        ← renderCustomerTable(customers, tbody)
    │   └── orders.js             ← renderOrdersTable(orders, tbody)
    │
    └── pages/
        ├── customers.js        ← wires DOM + api/customers + render/customers together
        └── orders.js             ← wires DOM + api/orders + render/orders together
```

💡 **WHY split `api/` into `client.js` + one file per resource:** `client.js` holds the one thing every resource shares — the base URL, headers, and error handling. `customers.js` and `orders.js` each just call `apiRequest(path, options)` and stay tiny. Adding a third resource later (`portfolio`, say) means adding `api/portfolio.js`, `render/portfolio.js`, `pages/portfolio.js`, and `portfolio.html` — nothing existing has to change.

### Two small additions to `customers.html`

Your uploaded HTML is almost ready — it just needs **hooks for JavaScript to find things**. Two changes:

1. Give the `<tbody>` an `id` (it currently has none):
   ```html
   <tbody id="customer-table-body" class="divide-y divide-gray-100">
   ```
2. Add a hidden field to track "which customer am I editing?", and `id`s on the form's title and buttons:
   ```html
   <h2 id="form-title" class="text-lg font-semibold text-gray-800 mb-4">Add Customer</h2>
   <form id="customer-form" class="space-y-4">
       <input type="hidden" id="customerId" value="">
       ...
       <button type="submit" id="save-btn" class="...">Save Customer</button>
       <button type="button" id="cancel-btn" class="...">Cancel</button>
   ```
3. Load your JS as a module, right before `</body>`:
   ```html
   <script type="module" src="scripts/pages/customers.js"></script>
   </body>
   ```
4. Link the stylesheets in `<head>`, alongside the Tailwind CDN script:
   ```html
   <script src="https://cdn.tailwindcss.com"></script>
   <link rel="stylesheet" href="styles/base.css">
   <link rel="stylesheet" href="styles/customers.css">
   ```
   `base.css` holds anything shared across every page; `customers.css` holds overrides unique to this page only (it can stay empty if Tailwind utility classes cover everything, as they do here).

⚠️ **GOTCHA:** the original table has 2 **hardcoded** `<tr>` rows inside `<tbody>`. Once JS starts rendering from the backend, those hardcoded rows should be **removed** — leave `<tbody id="customer-table-body"></tbody>` empty in the HTML. Otherwise you'll briefly see stale hardcoded data flash before real data replaces it.

### Start the backend

Following `CUSTOMERAPP-SETUP.md`:
```bash
cd flask-api
python3 app.py
```
Confirm it's up:
```bash
curl http://localhost:5050/api/customers
```
```json
[
  { "id": 1, "name": "Alex Rivera", "...": "..." },
  { "id": 2, "name": "Sara Kovacs", "...": "..." }
]
```

### Serve the frontend — don't just double-click `customers.html`

`<script type="module" src="scripts/pages/customers.js">` is blocked by the browser when loaded over `file://` — modules require `http://`, even locally. So `customers.html` needs its own tiny local server too, separate from Flask.

From inside `dom-flask-tailwind/` (wherever `customers.html` and the `scripts/`/`styles/` folders live), pick whichever tool you have available:

**Option A — Python (already installed if you followed this guide):**
```bash
cd dom-flask-tailwind
python3 -m http.server 8000
```

**Option B — Node:**
```bash
cd dom-flask-tailwind
npx serve -l 8000
```

**Option C — VS Code's "Live Server" extension** — right-click `customers.html` → "Open with Live Server." No terminal command needed.

Then open:
```
http://localhost:8000/customers.html
```
**Not** `file:///...` — it must be `http://localhost:...`.

⚠️ **GOTCHA — two servers running at once, and that's expected:**
- `http://localhost:5050` → Flask (the API)
- `http://localhost:8000` → whatever's serving the HTML/JS files (the frontend)

This is exactly the "different origins" situation `Flask-Cors` exists to solve (see `CUSTOMERAPP-SETUP.md`) — `api.js`'s `fetch('http://localhost:5050/...')` calls across that gap, and `CORS(app)` in `app.py` is what makes the browser allow it. If you forget to start the Flask server, the page loads fine but the table stays empty with a network error in the console — check DevTools (F12) → Console tab if that happens.

---

## Step 1 — Load the Table from the Backend (GET only)

Goal for this step: **just get real data on the page.** No form logic yet.

### `scripts/render/customers.js`

```javascript
const BRANCH_COLORS = {
    Budapest: 'bg-blue-50 text-blue-700',
    London: 'bg-purple-50 text-purple-700',
    Singapore: 'bg-emerald-50 text-emerald-700'
};

function formatBalance(balance) {
    return Number(balance).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function branchBadge(branch) {
    const colorClasses = BRANCH_COLORS[branch] || 'bg-gray-100 text-gray-700';
    return `<span class="${colorClasses} text-xs px-2 py-1 rounded-full">${branch ?? ''}</span>`;
}

function customerRowHtml(customer) {
    return `
        <tr class="hover:bg-gray-50" data-id="${customer.id}">
            <td class="px-4 py-3">${customer.id}</td>
            <td class="px-4 py-3 font-medium text-gray-800">${customer.name}</td>
            <td class="px-4 py-3">${customer.email}</td>
            <td class="px-4 py-3">${customer.phone ?? ''}</td>
            <td class="px-4 py-3">${customer.dob ?? ''}</td>
            <td class="px-4 py-3">${customer.joinDate ?? ''}</td>
            <td class="px-4 py-3">${branchBadge(customer.branch)}</td>
            <td class="px-4 py-3 text-right font-medium">${formatBalance(customer.balance ?? 0)}</td>
            <td class="px-4 py-3">
                <button class="text-indigo-600 hover:text-indigo-800 text-sm font-medium edit-btn" data-id="${customer.id}">Edit</button>
            </td>
        </tr>`;
}

export function renderCustomerTable(customers, tbodyElement) {
    tbodyElement.innerHTML = customers.map(customerRowHtml).join('');
}
```

💡 **WHY a separate `render.js` already, even for just this one step:** keeping "turn data into HTML" completely separate from "fetch the data" means this file never needs to know or care where the data came from — same principle as Track 4.

### `scripts/pages/customers.js` — Step 1 version

```javascript
import { renderCustomerTable } from '../render/customers.js';

const tbody = document.querySelector('#customer-table-body');

async function loadAndRenderCustomers() {
    const response = await fetch('http://localhost:5050/api/customers');
    const customers = await response.json();
    renderCustomerTable(customers, tbody);
}

await loadAndRenderCustomers();
```

### ✅ Verified — real output

Opening `customers.html` at this stage (with the Flask backend running):

```
Rows rendered: 2
```

The table now shows Alex Rivera and Sara Kovacs — pulled live from MySQL, not hardcoded — with the Tailwind styling (badge colors, hover states, right-aligned balance) fully intact.

---

## Step 2 — Capture Form Data (console.log first, no backend call yet)

Goal for this step: **prove you can correctly read every field**, before wiring anything to the network. This is a deliberate, separate step — debugging "is my form-reading code right?" is much easier without also debugging "is my fetch call right?" at the same time.

### Add this to `scripts/pages/customers.js`

```javascript
const form = document.querySelector('#customer-form');
const nameField = document.querySelector('#name');
const emailField = document.querySelector('#email');
const phoneField = document.querySelector('#phone');
const dobField = document.querySelector('#dob');
const joinDateField = document.querySelector('#joinDate');
const branchField = document.querySelector('#branch');
const balanceField = document.querySelector('#balance');

function readFormValues() {
    return {
        name: nameField.value,
        email: emailField.value,
        phone: phoneField.value,
        dob: dobField.value,
        joinDate: joinDateField.value,
        branch: branchField.value,
        balance: Number(balanceField.value) || 0
    };
}

form.addEventListener('submit', (event) => {
    event.preventDefault();     // stop the page from reloading
    console.log(readFormValues());   // just look at it for now — no fetch yet
});
```

⚠️ **GOTCHA:** `event.preventDefault()` is required from the very first version of this listener — without it, submitting the form reloads the page and your `console.log` never even gets a chance to run (covered back in Track 4, File 1, but easy to forget when starting a brand new file).

### ✅ Verified — real console output

Filling in the form (Name: "Tom Wilson", Email: "tom.wilson@example.com", Phone: "+1 555 0192", DOB: "1990-01-15", Join Date: "2026-01-01", Branch: "London", Balance: "3200") and clicking **Save Customer**:

```javascript
{
  name: 'Tom Wilson',
  email: 'tom.wilson@example.com',
  phone: '+1 555 0192',
  dob: '1990-01-15',
  joinDate: '2026-01-01',
  branch: 'London',
  balance: 3200
}
```

Notice `balance` printed as the **number** `3200`, not the string `"3200"` — confirming `Number(balanceField.value) || 0` worked correctly. This is exactly the shape the backend expects — you've confirmed that *before* ever making a network call.

---

## Step 3 — Send the Data to the Backend (Create)

Now replace the `console.log` with a real `POST` request.

### `scripts/api/customers.js` (using the shared `scripts/api/client.js`)

**`scripts/api/client.js`** — the one shared piece every resource will use:

```javascript
const BASE_URL = 'http://localhost:5050/api';

export async function apiRequest(path, options = {}) {
    const response = await fetch(`${BASE_URL}${path}`, {
        headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
        ...options
    });

    if (!response.ok) {
        let message = `Request failed: ${response.status}`;
        try {
            const errorBody = await response.json();
            message = errorBody.error || message;
        } catch {
            // response wasn't JSON — fall back to the generic message above
        }
        throw new Error(message);
    }

    if (response.status === 204) return null; // some DELETE responses have no body
    return response.json();
}
```

**`scripts/api/customers.js`** — the customers-specific calls, built on top of `client.js`:

```javascript
import { apiRequest } from './client.js';

export function getCustomers() {
    return apiRequest('/customers');
}

export function createCustomer(customer) {
    return apiRequest('/customers', { method: 'POST', body: JSON.stringify(customer) });
}
```

💡 **WHY move `getCustomers` into `scripts/api/customers.js` now too:** Step 1's inline `fetch` call inside the page script worked fine for one GET, but now that a second endpoint (`createCustomer`) is being added, it's the right moment to centralize every backend call for this resource in its own `api/` file — exactly the architecture from Track 4, now organized by resource.

### `scripts/pages/customers.js` — Step 3 version

```javascript
import { getCustomers, createCustomer } from '../api/customers.js';
import { renderCustomerTable } from '../render/customers.js';

const tbody = document.querySelector('#customer-table-body');
const form = document.querySelector('#customer-form');
// ...field references from Step 2...

async function loadAndRenderCustomers() {
    const customers = await getCustomers();
    renderCustomerTable(customers, tbody);
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const values = readFormValues();       // from Step 2
    await createCustomer(values);           // real POST now
    form.reset();
    await loadAndRenderCustomers();          // refresh the table to show the new row
});

await loadAndRenderCustomers();
```

### ✅ Verified — real output

Submitting the same Tom Wilson-style data (this run used "Priya Sharma" as the test record):

```
Rows before: 2
Rows after Add: 3
Last row: 3 Priya Sharma priya.sharma@example.com +44 7700 900123
1996-08-20 2026-08-01 Singapore 500.00 Edit
```

The new customer is now genuinely in MySQL — refreshing the page (a real reload, not just re-rendering in memory) would still show it.

---

## Step 4 — Edit & Update

Two parts: clicking **Edit** should populate the form; submitting while in "edit mode" should `PUT` instead of `POST`.

### Add `updateCustomer` to `scripts/api/customers.js`

```javascript
export function updateCustomer(id, updates) {
    return apiRequest(`/customers/${id}`, { method: 'PUT', body: JSON.stringify(updates) });
}
```

### `scripts/pages/customers.js` — Step 4 version

```javascript
import { getCustomers, createCustomer, updateCustomer } from '../api/customers.js';
// ...

const formTitle = document.querySelector('#form-title');
const saveBtn = document.querySelector('#save-btn');
const cancelBtn = document.querySelector('#cancel-btn');
const customerIdField = document.querySelector('#customerId');

function resetForm() {
    form.reset();
    customerIdField.value = '';
    formTitle.textContent = 'Add Customer';
    saveBtn.textContent = 'Save Customer';
}

function enterEditMode(customer) {
    customerIdField.value = customer.id;
    nameField.value = customer.name;
    emailField.value = customer.email;
    phoneField.value = customer.phone ?? '';
    dobField.value = customer.dob ?? '';
    joinDateField.value = customer.joinDate ?? '';
    branchField.value = customer.branch ?? '';
    balanceField.value = customer.balance ?? '';
    formTitle.textContent = `Edit Customer #${customer.id}`;
    saveBtn.textContent = 'Update Customer';
}

// ONE listener on the tbody catches Edit clicks for every row,
// including rows that didn't exist when the page first loaded
tbody.addEventListener('click', async (event) => {
    if (!event.target.classList.contains('edit-btn')) return;
    const id = Number(event.target.dataset.id);
    const customers = await getCustomers();
    const customer = customers.find(c => c.id === id);
    if (customer) enterEditMode(customer);
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const values = readFormValues();
    const editingId = customerIdField.value;

    if (editingId) {
        await updateCustomer(Number(editingId), values);   // PUT
    } else {
        await createCustomer(values);                        // POST
    }

    resetForm();
    await loadAndRenderCustomers();
});

cancelBtn.addEventListener('click', () => resetForm());
```

⚠️ **GOTCHA (same as Track 4):** the Edit listener is attached to the **tbody**, not to each `.edit-btn` individually — because `loadAndRenderCustomers()` replaces `tbody.innerHTML` on every refresh, destroying any listeners attached directly to old row elements. A listener on the parent survives every re-render.

### ✅ Verified — real output

```
--- after clicking Edit on the Priya Sharma row ---
Form title: Edit Customer #3
Name populated: Priya Sharma

--- after changing balance to 2500 and submitting ---
Last row: 3 Priya Sharma priya.sharma@example.com +44 7700 900123
1996-08-20 2026-08-01 Singapore 2,500.00 Edit
```

Note the form correctly switched to "Update Customer" mode, and the balance genuinely changed in MySQL (`500.00` → `2,500.00`), confirming this went through `PUT`, not a second `POST`.

---

## Step 5 — Delete

### Add a Delete button to `render.js`

```javascript
<td class="px-4 py-3 space-x-3">
    <button class="text-indigo-600 hover:text-indigo-800 text-sm font-medium edit-btn" data-id="${customer.id}">Edit</button>
    <button class="text-red-600 hover:text-red-800 text-sm font-medium delete-btn" data-id="${customer.id}">Delete</button>
</td>
```

### Add `deleteCustomer` to `scripts/api/customers.js`

```javascript
export function deleteCustomer(id) {
    return apiRequest(`/customers/${id}`, { method: 'DELETE' });
}
```

### `scripts/pages/customers.js` — final version, extending the same tbody listener

```javascript
import { getCustomers, createCustomer, updateCustomer, deleteCustomer } from '../api/customers.js';

tbody.addEventListener('click', async (event) => {
    const id = Number(event.target.dataset.id);
    if (!id) return;

    if (event.target.classList.contains('edit-btn')) {
        const customers = await getCustomers();
        const customer = customers.find(c => c.id === id);
        if (customer) enterEditMode(customer);
    }

    if (event.target.classList.contains('delete-btn')) {
        if (!confirm(`Delete customer #${id}? This cannot be undone.`)) return;
        await deleteCustomer(id);
        await loadAndRenderCustomers();
    }
});
```

💡 **WHY one `if` block for `id`, then separate `if`s for Edit vs. Delete:** both buttons carry `data-id`, so the guard at the top (`if (!id) return`) filters out clicks anywhere else in the row in one place, and the two `classList.contains(...)` checks below route to the right action — cleaner than duplicating the `id` extraction in two separate listeners.

⚠️ **GOTCHA:** `confirm(...)` is a **blocking, synchronous** browser dialog — it pauses all JavaScript execution until the user clicks OK/Cancel. That's normally undesirable in real apps (it freezes the whole page), but for a training exercise it's the simplest possible "are you sure?" safeguard, and it's genuinely fine for low-stakes internal tools. A polished production app would replace this with a custom modal instead.

### ✅ Verified — real output, full lifecycle

```
Rows on load: 2
Rows after Add: 3
Rows after Delete: 2
```

The full loop — load → add → edit → update → delete — was run end-to-end against the real Flask + MySQL backend, with every step producing genuine, persisted database changes, not just in-memory UI state.

---

## Recap: The Complete `scripts/pages/customers.js`

```javascript
import { getCustomers, createCustomer, updateCustomer, deleteCustomer } from '../api/customers.js';
import { renderCustomerTable } from '../render/customers.js';

const tbody = document.querySelector('#customer-table-body');
const form = document.querySelector('#customer-form');
const formTitle = document.querySelector('#form-title');
const saveBtn = document.querySelector('#save-btn');
const cancelBtn = document.querySelector('#cancel-btn');
const customerIdField = document.querySelector('#customerId');

const nameField = document.querySelector('#name');
const emailField = document.querySelector('#email');
const phoneField = document.querySelector('#phone');
const dobField = document.querySelector('#dob');
const joinDateField = document.querySelector('#joinDate');
const branchField = document.querySelector('#branch');
const balanceField = document.querySelector('#balance');

async function loadAndRenderCustomers() {
    const customers = await getCustomers();
    renderCustomerTable(customers, tbody);
}

function readFormValues() {
    return {
        name: nameField.value,
        email: emailField.value,
        phone: phoneField.value,
        dob: dobField.value,
        joinDate: joinDateField.value,
        branch: branchField.value,
        balance: Number(balanceField.value) || 0
    };
}

function resetForm() {
    form.reset();
    customerIdField.value = '';
    formTitle.textContent = 'Add Customer';
    saveBtn.textContent = 'Save Customer';
}

function enterEditMode(customer) {
    customerIdField.value = customer.id;
    nameField.value = customer.name;
    emailField.value = customer.email;
    phoneField.value = customer.phone ?? '';
    dobField.value = customer.dob ?? '';
    joinDateField.value = customer.joinDate ?? '';
    branchField.value = customer.branch ?? '';
    balanceField.value = customer.balance ?? '';
    formTitle.textContent = `Edit Customer #${customer.id}`;
    saveBtn.textContent = 'Update Customer';
}

tbody.addEventListener('click', async (event) => {
    const id = Number(event.target.dataset.id);
    if (!id) return;

    if (event.target.classList.contains('edit-btn')) {
        const customers = await getCustomers();
        const customer = customers.find(c => c.id === id);
        if (customer) enterEditMode(customer);
    }

    if (event.target.classList.contains('delete-btn')) {
        if (!confirm(`Delete customer #${id}? This cannot be undone.`)) return;
        await deleteCustomer(id);
        await loadAndRenderCustomers();
    }
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const values = readFormValues();
    const editingId = customerIdField.value;

    if (editingId) {
        await updateCustomer(Number(editingId), values);
    } else {
        await createCustomer(values);
    }

    resetForm();
    await loadAndRenderCustomers();
});

cancelBtn.addEventListener('click', () => resetForm());

await loadAndRenderCustomers();
```

---

## Step 6 — Scaling to Multiple Resources: Adding Orders

This is the payoff of the `api/` `render/` `pages/` split from Step 0 — a second resource, `orders`, added as a **dummy feature** to show the exact same pattern working for something that isn't customers. It's deliberately lighter than the customers feature (list + add only, no edit/delete) since its only job here is to demonstrate the structure scales.

### Backend: one more table, one more pair of routes

```sql
CREATE TABLE orders (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    customer_name  VARCHAR(120)  NOT NULL,
    item           VARCHAR(120)  NOT NULL,
    quantity       INT           NOT NULL DEFAULT 1,
    order_date     DATE,
    status         VARCHAR(30)   NOT NULL DEFAULT 'Pending',
    created_at     TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (customer_name, item, quantity, order_date, status) VALUES
('Alex Rivera', 'Laptop Stand', 2, '2026-07-15', 'Delivered'),
('Sara Kovacs', 'Wireless Mouse', 1, '2026-07-28', 'Shipped');
```

In `flask-api/app.py`, `GET /api/orders` and `POST /api/orders` follow the exact same shape as the customer routes — `serialize_order()` doing the same snake_case → camelCase conversion as `serialize_customer()`.

### `scripts/api/orders.js` — same `client.js`, new resource

```javascript
import { apiRequest } from './client.js';

export function getOrders() {
    return apiRequest('/orders');
}

export function createOrder(order) {
    return apiRequest('/orders', { method: 'POST', body: JSON.stringify(order) });
}
```

Notice this file has **zero knowledge of URLs, headers, or error handling** — all of that lives once in `client.js`, shared with `customers.js`.

### `scripts/render/orders.js` — same pattern as `render/customers.js`

```javascript
const STATUS_COLORS = {
    Pending: 'bg-amber-50 text-amber-700',
    Shipped: 'bg-blue-50 text-blue-700',
    Delivered: 'bg-emerald-50 text-emerald-700'
};

function statusBadge(status) {
    const colorClasses = STATUS_COLORS[status] || 'bg-gray-100 text-gray-700';
    return `<span class="${colorClasses} text-xs px-2 py-1 rounded-full">${status ?? ''}</span>`;
}

function orderRowHtml(order) {
    return `
        <tr class="hover:bg-gray-50" data-id="${order.id}">
            <td class="px-4 py-3">${order.id}</td>
            <td class="px-4 py-3 font-medium text-gray-800">${order.customerName}</td>
            <td class="px-4 py-3">${order.item}</td>
            <td class="px-4 py-3 text-right">${order.quantity}</td>
            <td class="px-4 py-3">${order.orderDate ?? ''}</td>
            <td class="px-4 py-3">${statusBadge(order.status)}</td>
        </tr>`;
}

export function renderOrdersTable(orders, tbodyElement) {
    tbodyElement.innerHTML = orders.map(orderRowHtml).join('');
}
```

### `scripts/pages/orders.js` — the thin orchestrator, same role as `pages/customers.js`

```javascript
import { getOrders, createOrder } from '../api/orders.js';
import { renderOrdersTable } from '../render/orders.js';

const tbody = document.querySelector('#orders-table-body');
const form = document.querySelector('#order-form');

async function loadAndRenderOrders() {
    const orders = await getOrders();
    renderOrdersTable(orders, tbody);
}

function readFormValues() {
    return {
        customerName: document.querySelector('#customerName').value,
        item: document.querySelector('#item').value,
        quantity: Number(document.querySelector('#quantity').value) || 1,
        orderDate: document.querySelector('#orderDate').value,
        status: document.querySelector('#status').value
    };
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const values = readFormValues();
    await createOrder(values);
    form.reset();
    await loadAndRenderOrders();
});

await loadAndRenderOrders();
```

### `orders.html` loads its own script and styles — completely independent of `customers.html`

```html
<link rel="stylesheet" href="styles/base.css">
<link rel="stylesheet" href="styles/orders.css">
...
<script type="module" src="scripts/pages/orders.js"></script>
```

Each page has a small nav link to the other (`customers.html` → "Orders →", `orders.html` → "← Customers"), so this is genuinely two separate pages — the multi-page structure from the planning discussion, in practice.

### ✅ Verified — real output, backend and frontend

**Backend, real curl:**
```
GET /api/orders →
[
  { "id": 1, "customerName": "Alex Rivera", "item": "Laptop Stand", "quantity": 2, "orderDate": "2026-07-15", "status": "Delivered" },
  { "id": 2, "customerName": "Sara Kovacs", "item": "Wireless Mouse", "quantity": 1, "orderDate": "2026-07-28", "status": "Shipped" }
]

POST /api/orders (missing fields) →
{ "error": "customerName and item are required" }   HTTP 400
```

**Frontend, real simulated Add flow:**
```
Rows on load: 2
Rows after Add: 3
Last row: 3 Tom Wilson Monitor 2 2026-08-04 Pending
```

Same architecture, same verification discipline, a second working resource — and notably, **nothing in the customers feature had to change** to add it.

### What adding a *third* resource (e.g. `portfolio`) would take

1. `portfolio` table + two routes in `app.py` (or move routes into a Flask Blueprint once `app.py` gets large — worth doing once you're past 3–4 resources)
2. `scripts/api/portfolio.js` — a few lines, using the same `apiRequest` from `client.js`
3. `scripts/render/portfolio.js` — one row-template function
4. `scripts/pages/portfolio.js` — the same thin orchestrator shape
5. `portfolio.html` + `styles/portfolio.css`

No file from `customers` or `orders` needs to be touched — that's the structural payoff this whole guide has been building toward.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Table stays empty, console shows a CORS error | `Flask-Cors` not enabled on the backend | Confirm `CORS(app)` is in `app.py` (see `CUSTOMERAPP-SETUP.md`) |
| Nothing loads at all, console error mentions modules + CORS + `file://` | Opened `customers.html` by double-clicking it instead of serving it | Serve it with `python3 -m http.server 8000` (or `npx serve`) and open `http://localhost:8000/customers.html` — see "Serve the frontend" above |
| Old hardcoded rows flash before real data loads | Hardcoded `<tr>` rows left in the HTML | Remove them — `<tbody id="customer-table-body"></tbody>` should start empty |
| Clicking Save reloads the page, nothing logs | Missing `event.preventDefault()` | Add it as the first line inside the `submit` listener |
| Edit button does nothing on newly added rows | Listener attached to individual buttons instead of the parent `tbody` | Use event delegation (Step 4) — one listener on `tbody`, not one per button |
| Balance shows `NaN` | Form field left empty, `Number("")` edge case not handled | Use `Number(value) || 0`, not `Number(value)` alone |