const fs = require('fs')
const express = require('express')
const app = express()
const port = 3000

/*
app.get('/', (request, response) => {
  response.send('Hello from Express!')
})
*/

app.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})


app.get('/', function(request, response){
    response.sendFile('/home/fyliu/github/problems/ai/duck/graph/index.html');
});
