
Easiest and fastest djikstra's algorithm

https://leetcode.com/problems/network-delay-time/discuss/109995

* Lang:    java
* Author:  SanD91
* Votes:   0

Create an adjacency list and a weight map and implement djikstra's. Start with node K, move to all its adjacent nodes with a weight w, add all adjacent to a queue and continue.
Adjacency list takes in O(n + m) space,
Avoided using a edge-weight matrix by using a map with key as 'source,destination', and  value as weight between source and destination. Reducing the space from O(n2) to O(m) where m is the number of edges.

```
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
	Map<Integer, List<Integer>> adj = new HashMap<>();
	Deque<Integer> dq = new ArrayDeque<>();
	Map<String, Integer> w = new HashMap<>();
	List<Integer> cur = new ArrayList<>();
        int[] dur = new int[N + 1];
        
        Arrays.fill(dur, Integer.MAX_VALUE);
        
        dur[K] = 0;
	int max = 0;
	int node = 0;
	int temp = 0;

	for(int[] time : times) {
            cur = new ArrayList<>();
            
	    if(adj.containsKey(time[0])) {
	        cur = adj.get(time[0]);
	    }

	    cur.add(time[1]);
     	    adj.put(time[0], cur);

	    w.put(time[0] + "," + time[1], time[2]);
	}

	dq.offer(K);

	while(!dq.isEmpty()) {
	    node = dq.poll();
	    temp = dur[node];
	    cur = adj.get(node);

	    if(cur != null && cur.size() > 0) {
	        for(int next : cur) {
                    if(dur[next] > w.get(node + "," + next) + temp) {
                        dur[next] = w.get(node + "," + next) + temp;
                        dq.offer(next);
                    }
		}
            }
        }

	for(int i = 1; i <= N; ++i) {
            if(dur[i] == Integer.MAX_VALUE) {
                return -1;
            }
            
	    max = Math.max(max, dur[i]);
	}

	return max;
    }
}
```
