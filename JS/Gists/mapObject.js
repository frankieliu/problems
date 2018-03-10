// https://stackoverflow.com/questions/19023226/map-over-object-preserving-keys
var _ = require('lodash');

console.log(_.mapValues({ one: 1, two: 2, three: 3 }, function (v) { return v * 3; }));


var mapped = _.reduce({ one: 1, two: 2, three: 3 }, function(obj, val, key) {
    obj[key] = val*3;
    return obj;
}, {});

console.log(mapped);

var obj = { one: 1, two: 2, three: 3 };
let newObj = Object.assign(...Object.keys(obj).map(k => ({[k]: obj[k] * 3})));
console.log(newObj);
