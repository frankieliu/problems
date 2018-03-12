function threeElementFunction (x, y, z) {
    console.log(x,y,z);
}

threeElementFunction(1,2,3);

function oneElementFunction(x) {
    console.log(x.color,x.shape,x.weight);
}

oneElementFunction(
    {color: "blue",
     shape: "wide",
     weight: "heavy"});

function passFunctionFunction(obj) {
    console.log(obj.f(2),obj.g(2),obj.h(2));
}

function square(x) {
    return x*x;
}

passFunctionFunction(square);
