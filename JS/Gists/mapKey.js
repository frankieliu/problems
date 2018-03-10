// https://stackoverflow.com/questions/455338/how-do-i-check-if-an-object-has-a-key-in-javascript

var pp = console.log;
var obj = {
    'key' : 2};
if ('key' in obj) {
    pp(true);
}

if ('nkey' in obj) {
    pp(false);
}

if ({}.hasOwnProperty.call(obj,'key')) {
    pp(true);
}

if (obj.hasOwnProperty('key')) {
    pp(true);
}
