
2 lines neat Python

https://leetcode.com/problems/wiggle-sort/discuss/71687

* Lang:    python3
* Author:  StefanPochmann
* Votes:   30

    def wiggleSort(self, nums):
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)
