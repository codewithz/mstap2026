// POST - create a new post (JSONPlaceholder's officially documented
// write-testing resource; same mechanics you'll use for /api/customers later)
async function addPost(post) {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify(post)
    });
    console.log('POST status:', response.status);
    const created = await response.json();
    console.log('Created:', created);
    return created;
}

// PUT - full update of an existing resource
async function updatePost(id, updates) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: 'PUT',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify({ id, ...updates })
    });
    console.log('PUT status:', response.status);
    const updated = await response.json();
    console.log('Updated:', updated);
}

// DELETE - remove a resource
async function deletePost(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: 'DELETE'
    });
    console.log('DELETE status:', response.status);
}

const newPost = await addPost({
    title: 'FSolutions Training Notes',
    body: 'Practicing POST requests against a real hosted API.',
    userId: 1
});

await updatePost(1, { title: 'Updated Title', body: 'Updated body', userId: 1 });
await deletePost(1);

// IMPORTANT: JSONPlaceholder fakes writes — it returns a realistic response
// (e.g. a new id) but nothing is actually saved on its server. This is
// intentional and documented, and is exactly why it's safe to practice on.