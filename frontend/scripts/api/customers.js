import { apiRequest } from "./client.js";

export function getCustomers(){
    return apiRequest("/customers")
}

export function createCustomer(customer){
    return apiRequest("/customers",{method:'POST',body: JSON.stringify(customer)})
}

export function updateCustomer(id, updates) {
    return apiRequest(`/customers/${id}`, { method: 'PUT', body: JSON.stringify(updates) });
}