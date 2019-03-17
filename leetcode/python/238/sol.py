
Python solution (Accepted), O(n) time, O(1) space

https://leetcode.com/problems/product-of-array-except-self/discuss/65625

* Lang:    python3
* Author:  hqpdash
* Votes:   216

    class Solution:
        # @param {integer[]} nums
        # @return {integer[]}
        def productExceptSelf(self, nums):
            p = 1
            n = len(nums)
            output = []
            for i in range(0,n):
                output.append(p)
                p = p * nums[i]
            p = 1
            for i in range(n-1,-1,-1):
                output[i] = output[i] * p
                p = p * nums[i]
            return output
