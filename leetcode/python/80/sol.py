
Python, 9 lines, 2 extra variables, 76ms. Any simpler solution else?

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/28128

* Lang:    python3
* Author:  qinhanlei
* Votes:   2

Skip the middle elements of the duplicates and rearrange the array.


    def removeDuplicates(self, nums):
            if len(nums) < 3: 
                return len(nums)
            pos = 1
            for i in range(1, len(nums)-1):
                if nums[i-1] != nums[i+1]:
                    nums[pos] = nums[i]
                    pos += 1
            nums[pos] = nums[-1]
            return pos + 1


The idea was pretty like solve [remove-duplicates-from-sorted-array][1] as below: 

    def removeDuplicates(self, nums):
            pos = 0
            for i in range(0, len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    nums[pos] = nums[i]
                    pos += 1
            return pos


  [1]: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
