
Python straightforward & self-explanatory & concise

https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/252596

* Lang:    python3
* Author:  cenkay
* Votes:   1

```
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, -heapq.heappop(A))
        return sum(A)
```
