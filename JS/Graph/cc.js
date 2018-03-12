// Load modules
var _ = require('lodash');

//----------------------------------------------------------------------
// Main data structure
// en : [[1, 2], ... ]
// e  : [['P','Q'], ... ]
var G ={
    en: [],  // numbered 
    e: []    // edges
};

//----------------------------------------------------------------------
// Add functionality to push edges into G.e
// add_edge(2,3) pushes [2,3] to an array
G.add_edge = function(x,y) {
    this.e.push([x,y]);
};

// Convert array to an object
// Converts [[colA, colB], ...] to {colA: colB, ...}
G.arrayToObject = function(val) {
    return val.reduce( function (result, item, index) {
	result[item[0]] = item[1]; return result; }, {});
};

// Change edge directivity so small -> large
// 3 -> 2 : 2 -> 3
G.sortVerticesInEdge = function (edges) {
    return _.map(
	edges,
	function(v) {
	    return (v[0] < v[1]) ? v : [v[1],v[0]];
	});
};

// Change edge directivity so large -> small
// 2 -> 3 : 3 -> 2
G.reverseSortVerticesInEdge = function (edges) {
    return _.map(
	edges,
	function(v) {
	    return (v[0] > v[1]) ? v : [v[1],v[0]];
	});
};

// Sort all edges by V1 column the by V2 column where edges : V1 -> V2
// Sorted edges example;
// [0, 2] < 
// [1, 2] < 
// [1, 3] <
// [2, 3]
G.sortEdgesByVertices = function (edges) {
    return _.sortBy(
	edges,
	[function(o) { return o[0]; },
	 function(o) { return o[1]; }] );
};

// Remove identical rows
// ...              ...
// a     becomes    a
// a                b
// b                c
// b
// c
G.removeIdenticalNextRows = function (edges) {
    return edges.reduce(
	function(result, item, index){
	    if (result instanceof Array) {
		if (result.length > 0) {
		    if (_.isEqual(result[result.length-1], item)) {
			// console.log("non-unique", item);
			return result;
		    } else {
			result.push(item);
			return result;
		    }
		} else {
		    result.push(item);
		    return result;
		}
	    }
	    return result;
	}, []);
};

// remove duplicate rows
// first  : sort all vertices (make them all point the same way)
// second : sort all edges (based on the first vertex then on the second)
// third  : remove identical adjacent rows
// note   : original order is lost
G.uniquifyEdges = function (edges) {
    return G.removeIdenticalNextRows(
	G.sortEdgesByVertices(
	    G.sortVerticesInEdge(edges)));
};

// Adding edges
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
// console.log(G);

//----------------------------------------------------------------------
// Add locations of vertices
G.loc = 
{
  "Portugal": [
    325.3,
    666
  ],
  "Spain": [
    325.3,
    594
  ],
  "France": [
    325.3,
    522
  ],
  "Belgium": [
    236.3,
    450
  ],
  "Germany": [
    241.3,
    378
  ],
  "Italy": [
    399.3,
    378
  ],
  "Netherlands": [
    53.295,
    306
  ],
  "England": [
    450.3,
    666
  ],
  "Wales": [
    415.3,
    594
  ],
  "Scotland": [
    443.3,
    522
  ],
  "Switzerland": [
    397.3,
    306
  ],
  "Austria": [
    343.3,
    234
  ],
  "Czech Republic": [
    229.3,
    162
  ],
  "Slovakia": [
    292.3,
    90
  ],
  "Hungary": [
    339.3,
    18
  ],
  "Denmark": [
    244.3,
    306
  ],
  "Poland": [
    222.3,
    18
  ]
};
   
// console.log(JSON.stringify(G.loc, undefined, 2));

//----------------------------------------------------------------------
// Give a unique id for each location
G.id = Object.keys(G.loc).reduce(
    function (result, item, index) {
	result[item] = {'position' : G.loc[item],
			'id' : Math.floor(G.loc[item][1] + G.loc[item][0]*0.01)*100};
	return result;
    },{});

// Create a reverse id map
G.rid = Object.keys(G.id).reduce(
    function (result, item, index) {
	result[G.id[item].id] = {'name' : item,
				 'position' : G.id[item].position};
	return result;
    },{});
    
console.log(G.id);
console.log(G.rid);

//----------------------------------------------------------------------
// Create the edge graph with the id's
G.en = _.map(G.e, p => [G.id[p[0]].id, G.id[p[1]].id]);
// console.log(G.en);


//----------------------------------------------------------------------
// Unit test : adding extra edge and see it being removed

function test_graph() {
    // Add and extra row:
    G.en.push([ 2139, 9292 ]);

    var sortEdge = function (v) {
	return (v[0] < v[1]) ? v : [v[1],v[0]]; };

    console.log("Sorted the edges, first vertex is always smaller than second vertex.");
    G.enSorted0 = _.map(G.en, sortEdge);
    // console.log(G.enSorted0);
   
    console.log("Finding unique elements: ");
    console.log("1. Sort by first // commentlumn , then by the second column");
    G.enSorted = _.sortBy(G.enSorted0,
			  [function(o) { return o[0]; }, function(o) { return o[1]; }]);
    // console.log(G.enSorted);

    console.log("2. Remove items which match previous inserted item.");
    // The problem is that I was returning result.push which is not an Array!
    G.euniq = (G.enSorted).reduce(
	function(result, item, index){
	    if (result instanceof Array) {
		if (result.length > 0) {
		    if (_.isEqual(result[result.length-1], item)) {
			console.log("non-unique", item);
			return result;
		    } else {
			result.push(item);
			return result;
		    }
		} else {
		    result.push(item);
		    return result;
		}
	    }
	    return result;
	}, []);
    console.log(G.euniq);
    console.log("----------------------------------------------------------------------");
}

function test_graph_uniquifyEdges() {
    // Add and extra row:
    G.en.push([ 2000, 9200 ]);
    G.enUniq = G.uniquifyEdges(G.en);
    console.log(G.en);
    console.log(G.enUniq);
}

test_graph_uniquifyEdges();

// Small star
// Change edge directivity so large -> small
G.enRev = G.reverseSortVerticesInEdge(G.en);
console.log(G.enRev);

function arrayMin(arr) {
  return arr.reduce(function (p, v) {
    return ( p < v ? p : v );
  });
}

function arrayMax(arr) {
  return arr.reduce(function (p, v) {
    return ( p > v ? p : v );
  });
}

// Suffle
var g = [[1,8],[5,8],[7,8],[8,9]];

var g1 = _.map(g, v => (v[0] > v[1]) ? v : [v[1],v[0]]);

// Reduce step < u, N(u) > , find min
var g2 = g1.reduce(
    function (result, current, index) {
	var left = current[0];
	var right = current[1];
	if (!(left in result)) {
	    result[left]={
		"neighbors" : [left],
		"min" : left};
	}
	result[left].neighbors.push(right);
	var curmin = result[left].min;
	result[left].min = (right < curmin) ? right : curmin;
	return result;
    },
    {});

function concatIfNonEmpty(arr1, arr2) {
    arr2.forEach(
	x => {
	    if (x != null) {
		arr1.push(x);
	    }
	});
    return arr1;
}

// Emit new edges, it is a flatmap
var g3 = Object.keys(g2).reduce(
    function (result, current, index) {
	var row = g2[current];
	return concatIfNonEmpty(result,
	    _.map(row.neighbors,
		  x => (x == row.min)? null : [x, row.min]));
    }, []);

// var g4 = _.mapValues(g2)
console.log(g);
console.log(g1);
console.log(g2);
console.log(g3);
