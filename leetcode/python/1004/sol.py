
Python Two Pointer One Pass O(n)

https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247600

* Lang:    python3
* Author:  joinyoung
* Votes:   0

Use two pointers `left` and `right` to indicate the sliding window.
Use `count` to count the number of 0s not used yet.
```
from collections import deque
class Solution(object):
    def longestOnes(self, A, K):
        if sum(A) + K >= len(A): return len(A)
        maximum = 0
        count = K
        right = 0
        for left in range(0, len(A) - K):
            while right < len(A) and (count > 0 or A[right] == 1):
                if A[right] == 0: count -= 1
                right += 1
                maximum = max(maximum, right - left)
            if right == len(A): break
            if A[left] == 0: count += 1
        return maximum
```
