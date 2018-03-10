// https://stackoverflow.com/questions/17822437/pipe-to-stdout-and-writeable-stream

var fs = require('fs');
console.log("hello").pipe(process.stdout);
