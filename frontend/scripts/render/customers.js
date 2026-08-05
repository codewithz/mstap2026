const BRANCH_COLORS = {
    Budapest: 'bg-blue-50 text-blue-700',
    London: 'bg-purple-50 text-purple-700',
    Singapore: 'bg-emerald-50 text-emerald-700'
};

function formatBalance(balance) {
    return Number(balance).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function branchBadge(branch) {
    const colorClasses = BRANCH_COLORS[branch] || 'bg-gray-100 text-gray-700';
    return `<span class="${colorClasses} text-xs px-2 py-1 rounded-full">${branch ?? ''}</span>`;
}

function customerRowHtml(customer) {
    return `
        <tr class="hover:bg-gray-50" data-id="${customer.id}">
            <td class="px-4 py-3">${customer.id}</td>
            <td class="px-4 py-3 font-medium text-gray-800">${customer.name}</td>
            <td class="px-4 py-3">${customer.email}</td>
            <td class="px-4 py-3">${customer.phone ?? ''}</td>
            <td class="px-4 py-3">${customer.dob ?? ''}</td>
            <td class="px-4 py-3">${customer.joinDate ?? ''}</td>
            <td class="px-4 py-3">${branchBadge(customer.branch)}</td>
            <td class="px-4 py-3 text-right font-medium">${formatBalance(customer.balance ?? 0)}</td>
            <td class="px-4 py-3">
               <button class="text-indigo-600 hover:text-indigo-800 text-sm font-medium edit-btn" data-id="${customer.id}">Edit</button>
    <button class="text-red-600 hover:text-red-800 text-sm font-medium delete-btn" data-id="${customer.id}">Delete</button>
            </td>
        </tr>`;
}

export function renderCustomerTable(customers, tbodyElement) {
    tbodyElement.innerHTML = customers.map(customerRowHtml).join('');
}