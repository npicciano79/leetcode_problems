//2620 counter
/*
---given an interger n, return a counter function 
---this counter function initially returns n
---then returns 1 more than the previous value 
---every subsquent time it is called (n, n+1, n+2,..)
*/

var createCounter=function(n){
    let count=0;
    let temp=0
    return function(){
        if (count==0){
            count+=1
            temp=n
            return n 
        }else{
            return temp+=1
        }
    }
}


const counter = createCounter(10)
console.log(counter())
console.log(counter())
console.log(counter())