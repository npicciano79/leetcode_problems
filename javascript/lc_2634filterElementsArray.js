//2634 filter elements from array
/*
given an array of integers arr and a filterning function fn, 
return a new array with fewer or equal number of elements 
without builtin array.filter method
*/

var filter=function(arr,fn){
    const tempArray=[]

    for (let i=0;i<=arr.length-1;i++){
        if(fn(arr[i],i)){
            tempArray.push(arr[i])
        }
    }
    return tempArray;
}
const arr=[0,10,20,30]
const fn=function greaterThan10(n){
    return n>10;
}

console.log(filter(arr,fn))