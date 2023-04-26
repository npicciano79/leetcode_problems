//2626 array reduce transformation 
/*
---given an integer array nums, a reducer function fn, and an initial val init
---return a reduced array 
*/


var reduce=function(num,fn,init){
    for (const num of nums){

        init=fn(init,num)

    }

    return init;


}