// // 
//     const nameOfObject = {
//         key: value,
//         key:value
//     }

const person= {
    name: 'Zartab M Nakhwa',
    age:36,
    youtube:'www.youtube.com/CodeWithZ',
    isMarried:true,
    letsCode(){
        console.log("Lets Start Coding..")
    }
}

console.log(person)
person.letsCode()

// Modify an object
//  1. Dot Operator 

person.qualification="Masters in Information Technology";
console.log(person)

// 2. Square Object

person["color"]="Black"
console.log(person)

// objectName[propertyName]=propertyValue

let propertyName="city"
let propertyValue="Mumbai"

person[propertyName]=propertyValue
console.log(person)

const countryCapitals={}

const countries=["India","SriLanka","UAE"]
const capitals=["New Delhi","Colombo","Abu Dhabi"]

let counter=0;

for(let country of countries){
    console.log(country)
    countryCapitals[country]=capitals[counter];
    counter++;
}

console.log(countryCapitals)