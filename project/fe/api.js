const BASE_URL = 'http://localhost:5050/api/customers';

export async function getCustomers() {
    const response = await fetch(BASE_URL);
    if (!response.ok) throw new Error(`Failed to load customers: ${response.status}`);
    return response.json();
}

export async function createCustomer(customer) {
    const response = await fetch(BASE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customer)
    });
    if (!response.ok) {
        const errorBody = await response.json();
        throw new Error(errorBody.error || `Failed to create customer: ${response.status}`);
    }
    return response.json();
}

export async function updateCustomer(id, updates) {
    const response = await fetch(`${BASE_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates)
    });
    if (!response.ok) throw new Error(`Failed to update customer ${id}: ${response.status}`);
    return response.json();
}

export async function deleteCustomer(id) {
    const response = await fetch(`${BASE_URL}/${id}`, { method: 'DELETE' });
    if (!response.ok) throw new Error(`Failed to delete customer ${id}: ${response.status}`);
    return response.json();
}
