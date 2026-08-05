import { getCustomers, createCustomer, updateCustomer, deleteCustomer } from './api.js';
import { renderCustomerTable } from './render.js';

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

// Event delegation: one listener on the tbody handles Edit AND Delete
// clicks for every row, including rows added after page load.
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