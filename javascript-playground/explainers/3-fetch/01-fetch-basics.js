// GET all users (JSONPlaceholder's /users resource — id, name, email, phone
// map closely to a "customer" shape, which is why we use it here)
async function loadAllUsers() {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    console.log('Status:', response.status, response.ok);
    const users = await response.json();
    console.log('Total users:', users.length);
    console.log('First user:', users[0]);
}

// GET a single user by id
async function loadOneUser(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await response.json();
    console.log(`User ${id}:`, user);
}

await loadAllUsers();
await loadOneUser(2);