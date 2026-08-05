import { renderCustomerTable } from '../render/customers.js';

const tbody = document.querySelector('#customer-table-body');

async function loadAndRenderCustomers() {
    const response = await fetch('http://localhost:5050/api/customers');
    const customers = await response.json();
    renderCustomerTable(customers, tbody);
}

await loadAndRenderCustomers();