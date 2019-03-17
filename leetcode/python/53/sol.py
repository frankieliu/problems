
A Python solution

https://leetcode.com/problems/maximum-subarray/discuss/20194

* Lang:    python3
* Author:  Google
* Votes:   144

    class Solution:
        # @param A, a list of integers
        # @return an integer
        # 6:57
        def maxSubArray(self, A):
            if not A:
                return 0
    
            curSum = maxSum = A[0]
            for num in A[1:]:
                curSum = max(num, curSum + num)
                maxSum = max(maxSum, curSum)
    
            return maxSum
