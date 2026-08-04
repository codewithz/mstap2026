function sayHello(){
    console.log("Welcome to Arrow Functions")
}

sayHello();

// -> Arrow
// => Fat Arrow

 ()=>{
    console.log("Welcome to Arrow Functions")
}

// Passed as a parameter in a function
// Assigned to a  variable

const myFirstArrow= ()=>{
    console.log("Welcome to Arrow Functions   =>")
};

myFirstArrow()

function squareTheNumber(number){
    return number*number;
}

 (number)=>{
    return number*number;
}

//  If the function only have one parameter, we can skip the ()
// 0 param -- ()   required
// 1 param -- ()  optional
//1+ param -- ()  required

number => {return number*number};

// if the function only have one statement
//  we can get rid of {} and return keyword
//  {} and return keyword will be absent or present together

//  if statement is console.log() -- it will be executed
// if the statement is number*number -- it will be returne


const square= number => number*number;

console.log(square(3))

function addMe(a,b,c){
    return a+b+c
}

 (a,b,c)=>a+b+c


 function calcualtion(x,y,z){
    const a=x+y+z;
    const b=y+5;
    const c=z-b;

    return a+b+c;
 }



 
  (x,y,z)=>{
    const a=x+y+z;
    const b=y+5;
    const c=z-b;

    return a+b+c;
 }
