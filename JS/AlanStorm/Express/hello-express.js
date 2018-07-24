//File: hello-express.js
console.log("Started Program");
var express = require('express');
var pug     = require('pug');

var app = express();


app.get('/', function (request, response) {
    console.log("Handling Request");    
    var html = pug.renderFile('page.pug',{
        'message':'Hello Pug!'
    });
    response.send(html);

    console.log("Done Handling Request");
});


app.listen(8000);
console.log("Ended Program");
