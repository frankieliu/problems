
Python bucket sort TLE ?

https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109097

* Lang:    python3
* Author:  yorkshire
* Votes:   1

How can this be improved? Seems to be O(n^2) and accepted in other languages.

```
    def smallestDistancePair(self, nums, k):
        diffs = [0 for _ in range(1000000)]
        
        for i, num in enumerate(nums):
            for num2 in nums[i + 1:]:
                diffs[abs(num - num2)] += 1
                
        for i, diff in enumerate(diffs):
            k -= diff
            if k <= 0:
                return i
```
