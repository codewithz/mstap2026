const numbers=[1,2,3,4,5,6,7,8,9,10]

const evenNumbers=[];

for (let number of numbers){
    if(number%2==0){
        evenNumbers.push(number)
    }
}

console.log("O:",numbers)
console.log("E:",evenNumbers)

// Higher order functions are which can accept another function as an input or return one

// 1. WHAT -- FIlter -- Array.filter --if will accept a function which returns a boolean ..apply on each element of array and keep those who pass the condition and reject those whol fails the condition

 // 2. HOW  -- Filter Even Numbers | Filter Odd Numbers


 function filterOdd(number){
    return number%2==1
 }

 const oddNumbers=numbers.filter(filterOdd)
 console.log("Odd:",oddNumbers)

 const divisibleByTHree=numbers.filter((number)=>number%3==0)
 console.log("Three:",divisibleByTHree)