const promise=new Promise(
   ( functionToBeInvokedWhenPromiseIsFulfilled,functionToBeInvokedWhenPromiseIsBroken)=>{
        console.log("Task to be performed -- Async Task");
        const isTaskSuccessful=false;
        if(isTaskSuccessful){
            functionToBeInvokedWhenPromiseIsFulfilled(10);
        }else{
            functionToBeInvokedWhenPromiseIsBroken(20)
        }
})
//---------------------------------------------------------------------------------------
promise
.then((valueReturnedWhenPromiseIsFulfilled)=>{
    console.log("Promise Fulfilled with value returned as :",valueReturnedWhenPromiseIsFulfilled);
})
.catch((valueReturnedWhenPromiseIsBroken)=>{
    console.log("Promise Broken with value returned as :",valueReturnedWhenPromiseIsBroken)
});

// -------------------------------------------------------------------------

const p=new Promise(
    (resolve,reject)=>{
        setTimeout(()=>{
            console.log("Task Happeneing");
            const data=[1,2,3,4];
            if(data){
                resolve(data)
            }else{
                reject(new Error("Data not loaded yet!!"))
            }
        },3000)
    }
)


p
.then((result)=>{
    console.log("Data Returned:",result)
})
.catch((error)=>{
    console.log(error.message)
})