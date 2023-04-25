//2635 apply transform over each element in array
/*
given an integer array arr and a mapping function fn
return a new array with a transformation applied to 
each element
*/

var map=function(arr,fn){
    var newArr=[];

    for (let i=0;i<=arr.length;i++){
        newArr.push(fn(arr[i],i))
    }
    return newArr;


}

var arr=[1,2,3]
var fn=function plusone(n){
    return n+1;
}

console.log(map(arr,fn));