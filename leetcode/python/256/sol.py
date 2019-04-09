
1+ lines Ruby, Python

https://leetcode.com/problems/paint-house/discuss/68209

* Lang:    python3
* Author:  StefanPochmann
* Votes:   19

First two solutions could easily be generalized to arbitrary number of colors.

**Solution 1** ... **Ruby**

    def min_cost(costs)
      costs.reduce([0]*3) { |prev, now| now.map { |n| n + prev.rotate![0,2].min } }.min
    end

**Solution 2** ... **Python**

    def minCost(self, costs):
        prev = [0] * 3
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(3)]
        return min(prev)

**Solution 3** ... **Python**

    def minCost(self, costs):
        return min(reduce(lambda (A,B,C), (a,b,c): (a+min(B,C), b+min(A,C), c+min(A,B)),
                          costs, [0]*3))
