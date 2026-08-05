import { renderCustomerTable } from '../render/customers.js';
import { getCustomers,createCustomer,updateCustomer,deleteCustomer } from '../api/customers.js';
const tbody = document.querySelector('#customer-table-body');

async function loadAndRenderCustomers() {
   
    const customers = await getCustomers();
    renderCustomerTable(customers, tbody);
}



const form= document.querySelector("#customer-form");
const nameField= document.querySelector("#name");
const emailField= document.querySelector("#email");
const phoneField= document.querySelector("#phone");
const dobField= document.querySelector("#dob");
const joinDateField= document.querySelector("#joinDate");
const branchField= document.querySelector("#branch");
const balanceField= document.querySelector("#balance");

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

function readFormValues(){
    return {
        name:nameField.value,
        email:emailField.value,
        phone:phoneField.value,
        dob:dobField.value,
        joinDate:joinDateField.value,
        branch:branchField.value,
        balance:Number(balanceField.value) || 0
    };
}

// ONE listener on the tbody catches Edit clicks for every row,
// including rows that didn't exist when the page first loaded
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
        await updateCustomer(Number(editingId), values);   // PUT
    } else {
        await createCustomer(values);                        // POST
    }

    resetForm();
    await loadAndRenderCustomers();
});

cancelBtn.addEventListener('click', () => resetForm());

await loadAndRenderCustomers();