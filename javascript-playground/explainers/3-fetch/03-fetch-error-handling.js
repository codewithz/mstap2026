// Case 1: HTTP error (404) — fetch does NOT throw, you must check response.ok
// JSONPlaceholder only has 10 users (ids 1-10), so id 999 doesn't exist
async function loadMissingUser() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users/999');
        console.log('Status:', response.status, 'ok:', response.ok);
        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }
        const user = await response.json();
        console.log(user);
    } catch (error) {
        console.log('Caught error:', error.message);
    }
}

// Case 2: Genuine network error — a domain that does not resolve at all
async function loadFromDeadDomain() {
    try {
        const response = await fetch('https://this-domain-does-not-exist-fsolutions.invalid/api');
        console.log(response.status);
    } catch (error) {
        console.log('Caught network error:', error.message);
    }
}

await loadMissingUser();
await loadFromDeadDomain();