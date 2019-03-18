
Simple Python O(n) two pointer in place solution

https://leetcode.com/problems/remove-element/discuss/12306

* Lang:    python3
* Author:  softray
* Votes:   30

Starting from the left every time we find a value that is the target value we swap it out with an item starting from the right.  We decrement end each time as we know that the final item is the target value and only increment start once we know the value is ok.  Once start reaches end we know all items after that point are the target value so we can stop there.


      def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
