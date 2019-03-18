
1-liner, 3-liner, 4-liner

https://leetcode.com/problems/combinations/discuss/27024

* Lang:    python3
* Author:  StefanPochmann
* Votes:   51

**Library - AC in 64 ms**

First the obvious solution - Python already provides this functionality and it's not forbidden, so let's take advantage of it.

    from itertools import combinations
    
    class Solution:
        def combine(self, n, k):
            return list(combinations(range(1, n+1), k))

---

**Recursive - AC in 76 ms**

But doing it yourself is more interesting, and not that hard. Here's a recursive version.

    class Solution:
        def combine(self, n, k):
            if k == 0:
                return [[]]
            return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

Thanks to @boomcat for [pointing out](https://discuss.leetcode.com/post/242007) `to use range(k, n+1)` instead of my original `range(1, n+1)`.

---

**Iterative - AC in 76 ms**

And here's an iterative one. 

    class Solution:
        def combine(self, n, k):
            combs = [[]]
            for _ in range(k):
                combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
            return combs

---

**Reduce - AC in 76 ms**

Same as that iterative one, but using `reduce` instead of a loop:

    class Solution:
      def combine(self, n, k):
        return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                      range(k), [[]])
