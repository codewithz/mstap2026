// denoted by ...
//can be applied to an array or an object
//  array -- [...]
// object -- {...}


const first=[1,2,3]
console.log("First:",first)
const second=[4,5,6]
console.log("Second:",second)

const combined1=first.concat(second)
console.log("Combined:",combined1)
// [1,2,3,4,5,6]

// [1,2,3,a,4,5,6,b]

const combined2=first.concat('a').concat(second).concat('b')
console.log("Combined2:",combined2)

const output=[first,'a',second,'b']
console.log(output)

const spreaded=[...first,'a',...second,'b']
console.log(spreaded)

// Problem Statement

// const grades=["A","B","D","C"]
// console.log("Grades",grades);
// const sorted=grades.sort()
// console.log("Sorted:",sorted)
// console.log("After Sorting .. Original is :",grades)

//Solved
const grades=["A","B","D","C"]
console.log("Grades",grades);
const sorted=[...grades].sort()
console.log("Sorted:",sorted)
console.log("After Sorting .. Original is :",grades)

const person={name:'Tom',age:25,gender:'M'}

const professional={company:'Neueda',dept:'IT',role:'DEveloper'}

const details={...person,...professional}
console.log(details)