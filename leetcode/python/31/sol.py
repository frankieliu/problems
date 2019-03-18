
Two-pointer solution in python with detail expalanation

https://leetcode.com/problems/next-permutation/discuss/13894

* Lang:    python3
* Author:  pennlio
* Votes:   14

Credit goes to http://blog.csdn.net/m6830098/article/details/17291259

    class Solution(object):
        def nextPermutation(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            # Use two-pointers: two pointers start from back
            # first pointer j stop at descending point
            # second pointer i stop at value > nums[j]
            # swap and sort rest
            if not nums: return None
            i = len(nums)-1
            j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
            while i > 0:
                if nums[i-1] < nums[i]: # first one violates the trend
                  j = i-1
                  break
                i-=1
            for i in xrange(len(nums)-1, -1, -1):
                if nums[i] > nums[j]: # 
                    nums[i], nums[j] = nums[j], nums[i] # swap position
                    nums[j+1:] = sorted(nums[j+1:]) # sort rest
                    return
