//2648 generate fibonacci sequence
/*
write a generator function that returns a generator object
which yields the fibonacci sequence 
*/

var fibGenerator=function*(){
    var a=0,b=1
    yield a;
    yield b;
    
    while(true){
        var c=a+b
        yield c
        a=b
        b=c
    }
}


const gen=fibGenerator();
gen.next().value;
gen.next().value;