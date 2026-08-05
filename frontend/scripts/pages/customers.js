import { renderCustomerTable } from '../render/customers.js';

const tbody = document.querySelector('#customer-table-body');

async function loadAndRenderCustomers() {
    const response = await fetch('http://localhost:5050/api/customers');
    const customers = await response.json();
    renderCustomerTable(customers, tbody);
}

await loadAndRenderCustomers();

const form= document.querySelector("#customer-form");
const nameField= document.querySelector("#name");
const emailField= document.querySelector("#email");
const phoneField= document.querySelector("#phone");
const dobField= document.querySelector("#dob");
const joinDateField= document.querySelector("#joinDate");
const branchField= document.querySelector("#branch");
const balanceField= document.querySelector("#balance");

function readFormValue(){
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

form.addEventListener('submit',(event)=>{
        event.preventDefault();
        console.log(readFormValue())
});