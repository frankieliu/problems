
10-line Python solution, 104 ms

https://leetcode.com/problems/the-skyline-problem/discuss/61261

* Lang:    python3
* Author:  kitt
* Votes:   59

Use an infinite vertical line `x` to scan from left to right. If max height changes, record [x, height] in `res`. Online judge is using Python 2.7.9 and there's no max heap's push and pop method, so we can use a min heap `hp` storing `-H` as "max heap". Thanks to [this discussion][1], set comprehension is faster and shorter than `list(set((R, 0, None) for L, R, H in buildings))`.

    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]


  [1]: https://leetcode.com/discuss/37736/108-ms-17-lines-body-explained
