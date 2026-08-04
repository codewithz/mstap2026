
async function displayUserReposAndCommits(){
    try{
        const user=await getUser(1001);
        console.log(user)
        const repos=await getReposForUser(user);
        console.log(repos)
        for(let repo of repos){
            const noOfCommits=await getCommitsForRepo(repo);
            console.log("Repo:",repo," -- No of Commits:",noOfCommits)
        }
    }
    catch(error){
        console.log("Error:",error.message)
    }
}


displayUserReposAndCommits()


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








