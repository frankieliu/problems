
Python short in-place solution with comments.

https://leetcode.com/problems/move-zeroes/discuss/72012

* Lang:    python3
* Author:  caikehe
* Votes:   98

    
    # in-place
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
