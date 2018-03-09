// https://stackoverflow.com/questions/9229645/remove-duplicate-values-from-js-array?page=1&tab=active#tab-top
//https://stackoverflow.com/questions/9229645/remove-duplicate-values-from-js-array?page=2&tab=active#tab-top

// There is a great section in the middle using sort and set operations
// It would be nice to be able to use set

var a = [2,3,4,5,5,4];
console.log(a);
console.log(a.filter(function(value, index){ return a.indexOf(value) == index }));
console.log(a.filter((v,i) => a.indexOf(v) == i));

// I prefer this solution if the number of uniq elements is small
// This does much better than the one above
console.log(a.reduce(
    (prev,cur) => {
	if (prev.indexOf(cur) < 0) prev.push(cur);
	return prev;
    },[]));

// Or using a hash table
console.log(a.reduce(
    (prev,cur) => {
	if (prev.indexOf(cur) < 0) prev.push(cur);
	return prev;
    },[]));


console.log([ ...new Set(a) ]);

// This doesn't work
var b =[[1,2],[1,2]];
console.log([ ...new Set(b) ]);
