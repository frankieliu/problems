var _ = require('lodash');
var G = {
    en: [],  // numbered
    e: []    // edges
};

G.add_edge = function(x,y) {
};

// initial conditions
G.v = [[],[],[],[]];
G.visited = [false,false,true,false];
G.en =
    [[0,3],
     [0,1],
     [0,2],
     [1,3],
     [2,0],
     [2,1]];

// console.log(G.en[1]);
function edgeFn(G) {
    return function(edge) {
        let src = edge[0];
        let dst = edge[1];
        if (G.visited[src]) {
            if (!(_.includes(G.v[dst],src))) {
                G.visited[dst] = true;
                G.v[dst].push(src);
                return 1;
            }
        }
        g        return 0;
    };
}

var a;
do {
    var a = G.en.map( edgeFn(G) );
} while (_.sum(a) != 0);

console.log(G);
