#define FOR_EACH(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
struct state {
    int vertex, weight;
};

const int MAX = 1000;     // max number of vertices
vector<state> graph[MAX]; // adjacency list, g[i] - list of edges from vertex i
int dist[MAX];            // dist[i] - distance from source to vertex i
int n;                    // number of vertices in the graph

void dijkstra(int source) {

    // fill the block of memory with 63
    memset(dist, 63, sizeof(dist));

    dist[source] = 0;

    priority_queue<state> q;

    q.push((state){source, 0});

    while(!q.empty()) {
        // take the top
        state top = q.top(); q.pop();

        // it's weight is old, there is a new weight...
        if(top.weight > dist[top.vertex]) continue;

        // look at each edge from the top.vertex
        FOR_EACH(it, graph[top.vertex]) {

            int alt = dist[top.vertex] + it->weight;

            if (alt < dist[it->vertex]) {
                // update the distance to vertex since found
                // a cheaper weight
                q.push((state){it->vertex, dist[it->vertex] = alt});
            }
        }
    }
}
