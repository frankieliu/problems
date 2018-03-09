
var _ = require('../../node_modules/underscore');

var G ={};
G.en = [];
G.e = [];

G.add_edge = function(x,y) {
    this.e.push([x,y]);
};

G.add_edge("Portugal", "Spain");
G.add_edge("Spain","France");
G.add_edge("France","Belgium");
G.add_edge("France","Germany");
G.add_edge("France","Italy");
G.add_edge("Belgium","Netherlands");
G.add_edge("Germany","Belgium");
G.add_edge("Germany","Netherlands");
G.add_edge("England","Wales");
G.add_edge("England","Scotland");
G.add_edge("Scotland","Wales");
G.add_edge("Switzerland","Austria");
G.add_edge("Switzerland","Germany");
G.add_edge("Switzerland","France");
G.add_edge("Switzerland","Italy");
G.add_edge("Austria","Germany");
G.add_edge("Austria","Italy");
G.add_edge("Austria","Czech Republic");
G.add_edge("Austria","Slovakia");
G.add_edge("Austria","Hungary");
G.add_edge("Denmark","Germany");
G.add_edge("Poland","Czech Republic");
G.add_edge("Poland","Slovakia");
G.add_edge("Poland","Germany");
G.add_edge("Czech Republic","Slovakia");
G.add_edge("Czech Republic","Germany");
G.add_edge("Slovakia","Hungary");

console.log(G);

var loc = {'Portugal': [325.3, 666.0], 'Spain': [325.3, 594.0], 'France': [325.3, 522.0], 'Belgium': [236.3, 450.0], 'Germany': [241.3, 378.0], 'Italy': [399.3, 378.0], 'Netherlands': [53.295, 306.0], 'England': [450.3, 666.0], 'Wales': [415.3, 594.0], 'Scotland': [443.3, 522.0], 'Switzerland': [397.3, 306.0], 'Austria': [343.3, 234.0], 'Czech Republic': [229.3, 162.0], 'Slovakia': [292.3, 90.0], 'Hungary': [339.3, 18.0], 'Denmark': [244.3, 306.0], 'Poland': [222.3, 18.0]};

var val = _.mapObject(loc, (v,k) => Math.floor((v[1] + v[0]*0.01)*100));
var tmp = 'Portugal';
var p = loc[tmp];
var [x,y] = p;

console.log(x);
console.log(y);
console.log(val);
G.en = _.map(G.e, p => [val[p[0]], val[p[1]]]);

// Add and extra row:
G.en.push([ 2139, 9292 ]);
console.log("----------------------------------------------------------------------");
console.log(G.en);

var sortEdge = function (v) {
    if (v[0] < v[1]) {
	return v;
    } else {
	return [v[1], v[0]];
    }
};

console.log("----------------------------------------------------------------------");

console.log(_.map(G.en, sortEdge));

console.log("----------------------------------------------------------------------");

G.enSorted = _.uniq(_.map(G.en, sortEdge));

console.log(G.enSorted);

console.log("----------------------------------------------------------------------");

var uniquify = function (A) {
    return A;
};

console.log(_.uniq([1,2,3,4,5,5]));
var a=[[1,2],[1,2],3,4,5,5];
console.log(_.uniq(a));
console.log(_.map((v,i) => a.indexOf(v)));
console.log(a.indexOf(3));
