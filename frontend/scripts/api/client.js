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