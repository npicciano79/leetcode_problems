//2619 array prototype last
/*
write code that enhances all arrays such that you can call the array.last()
method on any array and it will return teh last element.  if there are 
no elements, the array should return -1
*/

Array.prototype.last=function(){
    return this.length>0 ? this[this.length-1] : -1;
}


const arr=[1,2,3,4,5,6,7]
console.log(arr.last())