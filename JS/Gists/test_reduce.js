var a = [1,2,3];

var b = a.reduce(
    function  (acc, cur) {
	if (acc instanceof Array) {
	    acc.push(cur);
	}
	return acc;
    },
    []);

console.log(a);
console.log(b);

// ----------------------------------------------------------------------

var names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];
var countedNames = names.reduce(
    function (allNames, name) { 
  if (name in allNames) {
    allNames[name]++;
  }
  else {
    allNames[name] = 1;
  }
  return allNames;
}, {});
console.log(countedNames);

// countedNames is:
// { 'Alice': 2, 'Bob': 1, 'Tiff': 1, 'Bruce': 1 }
