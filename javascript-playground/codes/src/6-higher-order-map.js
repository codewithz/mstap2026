const numbers=[1,2,3,4,5,6,7,8,9,10]

function doubleTheNumber(number){
    return number*2;
}

const doubled=numbers.map(doubleTheNumber)
console.log("Original:",numbers)
console.log("Doubled:",doubled)

const squared=numbers.map((number)=>number*number)
console.log("Squared:",squared)

// ---------------------------------------------------------------------------

const users=[
    {id:1,name:'User1',dept:'IT'},
    {id:2,name:'User2',dept:'IT'},
    {id:3,name:'User3',dept:'IT'},
    {id:4,name:'User4',dept:'IT'},
    {id:5,name:'User5',dept:'IT'},
]

{/* <div>
    <h1>Name</h1>
    <h1>Dept</h1>
    <h1>ID</h1>
    </div> */}


    function transformToComponent(user){
        return `
         <div>
    <h1>${user.name}</h1>
    <h1>${user.dept}</h1>
    <h1>${user.id}</h1>
    </div>
        `
    }

    const components=users.map(transformToComponent)
    console.log(users)
    console.log(components)