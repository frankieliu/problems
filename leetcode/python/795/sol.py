
Python One Pass

https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/253556

* Lang:    python3
* Author:  joinyoung
* Votes:   0

`Count1` counts the number of contigous elements bounded by `R`. `Count2` the number of elements bounded by `L-1`. 
```
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        count1, count2 = 0, 0
        res = 0
        for i, num in enumerate(A):
            if num <= R:
                count1 += 1
            else:
                res += count1 * (count1 + 1) // 2
                count1 = 0
            if num < L:
                count2 += 1
            else:
                res -= count2 * (count2 + 1) // 2
                count2 = 0
        res += count1 * (count1 + 1) // 2
        res -= count2 * (count2 + 1) // 2
        return res
```
