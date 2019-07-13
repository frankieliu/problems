In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1046.last-stone-weight.algorithms.json

[Java/Python] O(nlogn)

https://leetcode.com/problems/last-stone-weight/discuss/294956

* Lang:    python
* Author:  lee215
* Votes:   19

**Java, PriorityQueue**
```
    public int lastStoneWeight(int[] A) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b)-> b - a);
        for (int a : A)
            pq.offer(a);
        for (int i = 0; i < A.length - 1; ++i)
            pq.offer(pq.poll() - pq.poll());
        return pq.poll();
    }
```

**Python, Priority queue, o(nlogn) time**
```
    def lastStoneWeight(self, A):
        pq = [-x for x in A]
        heapq.heapify(pq)
        for i in xrange(len(A) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]
```

**Python, insort, o(n^2) time**
```
    def lastStoneWeight(self, A):
        stones = sorted(stones)
        for _ in xrange(len(stones) - 1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))
        return stones.pop()

```
