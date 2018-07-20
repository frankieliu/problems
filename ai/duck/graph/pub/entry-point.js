//#File: src-client/entry-point.js
helloWorld = require('./hello-world');

if(typeof alert !== 'undefined'){
    alert(helloWorld.getMessage());
}
else{
    console.log(helloWorld.getMessage());
}
