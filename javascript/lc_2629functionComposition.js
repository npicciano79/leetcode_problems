//2629 function composition 
/*
Given an array of functions [f1,f2,f3...fn]
return a new function fn, that is the function composition of 
the array of the functions

input: functions=[x => x + 1, x => x * x, x => 2 * x], x = 4
output:65

*/


var compose=function(functions){
    return function(x){
        let tempOut=x;
        for (let i=functions.length-1;i>=0;i--){
            tempOut=functions[i](tempOut)
        }
        return tempOut;
    }
}

const fn=compose([x => x + 1, x => x * x, x => 2 * x])
console.log(fn(4));