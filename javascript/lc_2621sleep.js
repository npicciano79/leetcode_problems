//2621 sleep
/*
---given an positive integer millis
---write an asncronous function that 
---sleeps for millis
*/

async function sleep(millis){
    return new Promise(resolve=>setTimeout(resolve,millis));
}

let t = Date.now()
sleep(100).then(()=>console.log(Date.now()-t))//100