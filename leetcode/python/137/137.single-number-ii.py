#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (44.88%)
# Total Accepted:    155.5K
# Total Submissions: 346.6K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        0,1,0,1,0,1,99
        """

        """

        a + s = ?

           Next sum:                Next carry:
           sa                       sa
           01   11  10 00           01   11  10 00
      c 0   1    0   1  0      c 0   0    1   0  0
        1   1    x   1  0        1   1    x   1  1


        ~s . a  +  s . ~a           ~s . c + s . a  + c . ~a


         sum:                      carry
           sc                    sc
           01 11 10 00           01 11 10 00
            0  0  1  0            1  0  0  0

           s & ~c                ~s & c


        putting these two steps together

        (~s . a + s . ~a) & ~(s . a + c . ~a)
                             ~(s.a) . ~(c.~a)
        (~s.a . ~(s.a) . ~(c.~a) +

        """

        # for each keep a count of each bit
        s = 0  # sum
        c = 0  # carry

        for a in nums:

            sn = (~s & a) | (s & ~a)
            cn = (s & a) | (c & ~(s & a))
            s = sn
            c = cn
            # print(bin(s), bin(c))
            sn = s & ~c
            cn = ~s & c
            s = sn
            c = cn
            # print(bin(s), bin(c))

        return(s)

test = False
if test:
    s = Solution()
    print(s.singleNumber([2,4,2,3,4,2,4]))
