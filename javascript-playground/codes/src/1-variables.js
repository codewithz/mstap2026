//  Re Assignment
//  Re Declaration
//  No Block Scoping

console.log("------------------------------- var ------------------------")

function understandingVar(){
    var name="Zartab";
    console.log(name);

    for(var index=1;index<=10;index++){
        console.log("Index=",index)
    }
    console.log("Outside the loop Index=",index)
    name="Dee";
    console.log("Name=",name)
    var name="Neueda";
    console.log("Name=",name)
}

understandingVar()

// ------------- let and const --------------
//  Re Assignment
//  No Declaration
//   Block Scoping

console.log("------------------------------- let ------------------------")

function understandingLet(){
    let name="Zartab";
    console.log(name);

    for(let index=1;index<=10;index++){
        console.log("Index=",index)
    }
    // console.log("Outside the loop Index=",index)
    name="Dee";
    console.log("Name=",name)
    name="Neueda";
    console.log("Name=",name)
}

understandingLet()


console.log("------------------------------- const ------------------------")
//  No Assignment
//  No Declaration
//   Block Scoping
function understandingConst(){
    const name="Zartab";
    console.log(name);

    // for(const index=1;index<=10;index++){
    //     console.log("Index=",index)
    // }
    // console.log("Outside the loop Index=",index)
    // name="Dee";
    // console.log("Name=",name)
    // name="Neueda";
    // console.log("Name=",name)
}

understandingConst()