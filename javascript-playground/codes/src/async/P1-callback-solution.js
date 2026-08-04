
console.log("Before")

getUser(1001,callbackFunctionForUser)


console.log("After")




function getUser(id,callback){
    // setTimeout(executesThisArrowFunction,afterWaitingForThisManyMilliseconds)
    setTimeout(()=>{
        console.log("Reading Id from Database...");
        const user= {id:id,gitUser:'codewithz'};
        callback(user)
    },2000)
}

function callbackFunctionForUser(user){
    console.log(user)
    getReposForUser(user,callbackFunctionForRepos)
}

function getReposForUser(user,callback){
    setTimeout(()=>{
        console.log("Connection to github.com [",user.gitUser,"]...");
        const listOfRepos=["mstap2024","mstap2025","mstap2026"];
        callback(listOfRepos)
    },3000)
}


function callbackFunctionForRepos(listOfRepos){
    for(let repo of listOfRepos){
        console.log(repo)
        getCommitsForRepo(repo,callbackFunctionForCommits)
    }
}


function getCommitsForRepo(repo,callback){
    setTimeout(()=>{
        console.log("COnnecting to repo:",repo)
        const noOfCommits=Math.floor(Math.random()*100)+1
        callback(noOfCommits)
    },2000)
}





function callbackFunctionForCommits(noOfCommits){
    console.log("Commits are ",noOfCommits)
}


// CALLBACK HELL