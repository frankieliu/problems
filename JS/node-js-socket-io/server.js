import express from 'express';
import path from 'path';
import bodyParser from 'body-parser';

const app = require('express')();
const server = require('http').Server(app);
const io = require('socket.io')(server);

const PORT = 3001;
server.listen(PORT);
console.log('Server is running');

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

const connections = [];
io.on('connection', (socket) => {
    socket.emit('news', { hello: 'world' });
    socket.on('my other event', (data) => {
              console.log(data);
             });
    connections.push(socket);
    console.log(' %s sockets are connected', connections.length);
});


