var _ = require('../../node_modules/underscore');

var arr1 = [1, 2, 3, 4];

console.log(_.map(arr1,x => [x * 2])); 
// [[2], [4], [6], [8]]

console.log(_.flatten(_.map(arr1, x => [x * 2])));
// [2, 4, 6, 8]

// only one level is flattened
console.log(_.flatten(_.map(arr1, x => [[x * 2]])));
// [[2], [4], [6], [8]]
