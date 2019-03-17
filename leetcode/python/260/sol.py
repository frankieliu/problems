
Python O(n) - O(1) solution

https://leetcode.com/problems/single-number-iii/discuss/68999

* Lang:    python3
* Author:  briankwong
* Votes:   3

    class Solution(object):
        def singleNumber(self, nums):
            # https://leetcode.com/discuss/48119/single-number-iii
            xor = 0
            for num in nums: xor ^= num
            xor = xor & (xor - 1) ^ xor
            a = b = 0
            for num in nums:
                if xor & num:
                    a ^= num
                else:
                    b ^= num
            return [a, b]
