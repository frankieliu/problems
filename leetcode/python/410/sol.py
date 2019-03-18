
Best Complexity - Double Binary Search - Beats 99.5% of solutions - Python Solution

https://leetcode.com/problems/split-array-largest-sum/discuss/89854

* Lang:    python3
* Author:  humachine
* Votes:   0

A lot of great solutions have been posted on this forum. Most of those solutions have the same skeleton: 
- Run a binary search on various maxSplit candidates between arrayMax and arraySum
- For each candidate you find during the binary search, check if it can lead to valid split of the array into <= m portions.
- Find the first maxLimit candidate for which there's a valid array split.

The complexity of the usual algorithm specified above  = **O(n \\* log(arraySum - arrayMax))**
The log(arraySum-arrayMax) comes from the binary search algorithm. And the multiplication by n comes from the greedy search which takes O(n) for each time.

Here, I propose a new solution which runs in **O(n + log(arraySum-arrayMax)\\*mlog(n))**. For large arrays, it's not unwise to expect that arraySum-arrayMax might bloat up.  

Taking some simple example cases with N=1,000,000 elements. And since we're dealing with non-neg numbers, it's not unusual to have arraySum in the order of N. 

The usual solution has a complexity of (N*O(arraySum-arrayMax))  ~~ **O(N * N)** in this case. 
This new solution's complexity would turn out to be *****O(N + logN * mlogN)****.


Here's the solution:
```
from bisect import bisect_right
class Solution(object):
    def validSplitBinary(self, nums, m, cumSums, maxSum):
    ''' Here, the greedy step of the solution is performed using a binary search on the cumulative sum array. So, the entire greedy validation takes O(mLogN time)
    '''
        curr, count, low = maxSum, 0, 0
        while low<len(cumSums):
            low = bisect_right(cumSums, curr, low) #Trying to find the location at which we get the best cumulative sum <= maxSum
            curr, count = cumSums[low-1] + maxSum, count+1
            if count>m: 
                  return False
        return True
        
    def splitArray(self, nums, m):
        arrayMax, cumSums, some = max(nums), [nums[0]], 0
        for i in xrange(1, len(nums)):
            cumSums.append(cumSums[i-1]+nums[i]) #cumSums - list of cumulative sums of array
        left, right = arrayMax, cumSums[-1]
        while left<right: #Binary Search Step
            mid = (left+right)/2
            if self.validSplitBinary(nums, m, cumSums, mid):
                right = mid
            else:
                left = mid+1
        return right
```

In this solution, validation of a maxLimit candidate is done using binary search instead of the lineary greedy approach. We the cumulative sums list to find sub-sections of the array, which each have sums < maxLimit.
