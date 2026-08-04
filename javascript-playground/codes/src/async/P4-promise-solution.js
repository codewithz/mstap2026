
console.log("Before")

const p=getUser(1001);

p
.then((user)=>{
    console.log("User:",user)
    return getReposForUser(user);
})
.then((repos)=>{
    console.log("Repos:",repos);
    for(let repo of repos){
        getCommitsForRepo(repo)
        .then(noOfCommits=>{
            console.log("No of commits:",noOfCommits)
        })
    }
})
.catch((error)=>{
    console.log("Error:",error.message)
})


console.log("After")




function getUser(id){

    const promise=new Promise(
        (resolve,reject)=>{
              // setTimeout(executesThisArrowFunction,afterWaitingForThisManyMilliseconds)
                setTimeout(()=>{
                    console.log("Reading Id from Database...");
                    const user= {id:id,gitUser:'codewithz'};
                    resolve(user)
                },2000)
        }
    );

    return promise;
  
}


function getReposForUser(user){
        const promise=new Promise(
        (resolve,reject)=>{
            setTimeout(()=>{
                console.log("Connection to github.com [",user.gitUser,"]...");
                const listOfRepos=["mstap2024","mstap2025","mstap2026"];
                resolve(listOfRepos)
            },3000)
        });

         return promise;
}





function getCommitsForRepo(repo){
        const promise=new Promise(
        (resolve,reject)=>{
            setTimeout(()=>{
                console.log("COnnecting to repo:",repo)
                const noOfCommits=Math.floor(Math.random()*100)+1
                resolve(noOfCommits)
            },2000)
        });

        return promise;
}








