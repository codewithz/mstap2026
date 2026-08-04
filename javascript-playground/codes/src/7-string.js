const name="Thomas";
const city="London";

const sentence=name+ " lives in "+city;
console.log(sentence)

// "" |  '' | ``

const paragraph=`Variables = Data Containers
JavaScript variables are containers for data.

JavaScript variables can be declared in 4 ways:

Modern JavaScript`

console.log(paragraph)

console.log("------------- String Interpolation--------")

const nameOFEmployee='Thomas'
const company='Neueda'
const employeeCode='N00001'

//Thomas works for Neueda and his employee code is N00001

const line=nameOFEmployee+" works for "+company+" and his employee code is "+employeeCode
console.log(line)

const iLine=`${nameOFEmployee} works for ${company} and his employee code is ${employeeCode}`
console.log(iLine)