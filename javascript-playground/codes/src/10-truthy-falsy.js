// Values are considered falsy -- evaluate to false

// 1. false
// 2. 0 -- the number zero
// 3. "" or ''  empty
// 4. null
// 5. undefined

function testTruthyOrFalsy(value){
    if(value){
        console.log("Truthy")
    }else{
        console.log("Falsy")
    }
}


let numberZero=0;
testTruthyOrFalsy(numberZero)

let number100=100;
testTruthyOrFalsy(number100)


let emptyString='';
testTruthyOrFalsy(emptyString)


let filledString='a';
testTruthyOrFalsy(filledString)

let blankArray=[];
testTruthyOrFalsy(blankArray)

let blankObject={};
testTruthyOrFalsy(blankObject)

//const data=null --> will not be populated until API from backed responsds

// if(data){
//     dispalayTable
// }else{
//     display a loader
// }