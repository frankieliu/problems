
Python, min-heap, O(n) space and almost O(n) time

https://leetcode.com/problems/third-maximum-number/discuss/244500

* Lang:    python3
* Author:  DanielLenz
* Votes:   0

```
from heapq import heappush, heappushpop

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Will have N*log(k) complexity, in this case log(k=3) = 1.09
        # Using O(N) space, giving us a unique representation of the input
        nums = set(nums)
        
        # Edgecase
        if len(nums) < 3:
          return max(nums)

        heap = []
        
        # Put 3 elements in our min-heap
        for _ in range(3):
          heappush(heap, nums.pop())
          
        # Pushpop remaining elements, giving us
        # the 3 largest unique elements from nums
        while nums:
          heappushpop(heap, nums.pop())
          
        return heap[0]
          
```
