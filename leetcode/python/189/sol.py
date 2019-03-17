
My simple python code

https://leetcode.com/problems/rotate-array/discuss/54427

* Lang:    python3
* Author:  Mayer5
* Votes:   10

    class Solution:
        def rotate(self, nums, k):
            while k > 0:
                nums.insert(0, nums.pop())
                k -= 1
