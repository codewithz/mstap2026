# Fetch · File 2: Sending Data (POST, PUT, DELETE)

`GET` just asks for data. To *create*, *update*, or *remove* something on the server, `fetch()` needs a second argument — an options object describing the HTTP method, headers, and the data you're sending.

Source: `src/fetch/02-fetch-sending-data.js` — against JSONPlaceholder's `/posts` resource, which is the officially documented endpoint their own guide uses for testing writes (`/users` supports reads well, but `/posts` is the endpoint JSONPlaceholder's docs specifically confirm and demonstrate for POST/PUT/PATCH/DELETE).

---

## 💡 The Concept

```javascript
async function addPost(post) {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify(post)
    });
    const created = await response.json();
    console.log('Created:', created);
    return created;
}
```

Three pieces every non-GET request needs:

| Option | Purpose |
|---|---|
| `method` | `'POST'`, `'PUT'`, `'DELETE'`, etc. (default is `'GET'` if omitted) |
| `headers: { 'Content-type': 'application/json' }` | Tells the server "the body I'm sending is JSON text" — without this, most backends (Flask included) won't parse the body correctly |
| `body: JSON.stringify(post)` | The actual data — **must** be a string, not a raw object; `JSON.stringify()` converts your JS object into JSON text |

🔁 **ANALOGY:** Sending a JS object directly as `body` (without `JSON.stringify`) is like mailing someone a piece of furniture fully assembled — it won't fit through the mail slot. `JSON.stringify()` flat-packs it into a string that travels over HTTP; the server then "assembles" it back into an object on its end (this is what Flask's `request.get_json()` does).

---

## 🎨 Diagram: POST → PUT → DELETE Lifecycle

```mermaid
flowchart LR
    classDef post fill:#4ECDC4,stroke:#1A8C82,color:#fff,font-weight:bold
    classDef put fill:#FFD93D,stroke:#B8860B,color:#2D3436,font-weight:bold
    classDef del fill:#FF6B6B,stroke:#C0392B,color:#fff,font-weight:bold

    A["POST /posts<br/>body: new record"]:::post --> B["Server assigns an id,<br/>responds 201 Created"]:::post
    B --> C["PUT /posts/id<br/>body: full replacement"]:::put
    C --> D["Server responds 200 OK<br/>with updated record"]:::put
    D --> E["DELETE /posts/id<br/>no body needed"]:::del
    E --> F["Server responds 200 OK"]:::del
```

⚠️ **GOTCHA — genuinely important, documented behavior of JSONPlaceholder:** every write (`POST`/`PUT`/`PATCH`/`DELETE`) returns a **realistic-looking, correctly-shaped response** — but nothing is actually saved on JSONPlaceholder's server. Their own docs state it plainly: *"resource will not be really updated on the server but it will be faked as if."* This is intentional and exactly why it's safe to hammer on: you get real HTTP status codes and real response shapes to build your error-handling logic against, with zero risk of leaving behind junk data. **This is different from your local mock server or your real Flask API later — both of those genuinely persist changes.**

**Documented output** (from JSONPlaceholder's official guide, confirmed current):
```
POST status: 201
Created: { id: 101, title: 'FSolutions Training Notes', body: 'Practicing POST requests...', userId: 1 }

PUT status: 200
Updated: { id: 1, title: 'Updated Title', body: 'Updated body', userId: 1 }

DELETE status: 200
```
Note `id: 101` on the created post — JSONPlaceholder has exactly 100 seed posts, so every simulated `POST` is documented to return `id: 101`, no matter how many times you run it (since nothing is actually persisted, the counter never really moves forward).

---

## PUT vs PATCH

JSONPlaceholder supports both:
- **`PUT`** expects the **full object** — every field, since it conceptually replaces the whole record.
- **`PATCH`** expects only the **fields you're changing** — a partial update.

💡 **WHY this matters for Track 4:** confirm with your Flask API's docs (or whoever built it) which one it expects — some REST APIs are strict about this distinction, others treat them the same. Don't assume.

---

## ✅ TRY THIS — Hands-On Practice

```javascript
async function updatePostTitle(id, newTitle) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: 'PATCH',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify({ title: newTitle })
    });
    const updated = await response.json();
    console.log(updated);
}

updatePostTitle(1, 'My New Title');
```

Try this directly in your browser console — it's a real, live request.

---

## 🧪 Lab

1. Write `addPost` with a `title`, `body`, and `userId`, and log the server-assigned `id` (should be `101`).
2. Write `updatePostTitle(id, newTitle)` using `PATCH`, sending only the `title` field.
3. Write `removePost(id)` using `DELETE`, and log the response status to confirm it succeeded.

---

## 🚀 Challenge Task

Chain all three together: add a post, immediately update one of its fields, then delete it — logging the state after each step. This exact create → update → delete sequence is what your Customer Management form's Add/Edit/Delete buttons will trigger in Track 4, just against your own Flask `/api/customers` endpoints instead of `/posts`.

*No solution provided — bring your attempt to the next session.*
