const address={
    city:'Mumbai',
    state: 'MH',
    pincode:400001,
    country:'India'
}

const state="Maharashtra"

// Traditional Way
// const city=address.city
// const state=address.state
// const pincode=address.pincode
// const country=address.country

const {city,pincode}=address
const {country,state:st}=address

console.log("A:",address)
console.log("City:",city)
console.log("Country:",country)
console.log("Pincode:",pincode)
console.log("State outside:",state)
console.log("State inside:",st)

console.log("------------- Function and Destructuring -----")

function displayAddress(address){
    console.log(address.city)
    console.log(address.state)
    console.log(address.country)
    console.log(address.pincode)

}

displayAddress(address)

console.log("----------------------------------------------------")

function displayAddressWithDestructuredObject({city,state,country,pincode}){
     console.log(city)
    console.log(state)
    console.log(country)
    console.log(pincode)
}

displayAddressWithDestructuredObject(address)