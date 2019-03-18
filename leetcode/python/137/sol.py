
Python Bit Manipulation  (with more general case)

https://leetcode.com/problems/single-number-ii/discuss/43412

* Lang:    python3
* Author:  briankwong
* Votes:   11

    class Solution(object):
        def singleNumber(self, nums):
            one, two = 0, 0
            for x in nums:
                one, two, three = one ^ x, two | (one & x), two & x
                one, two = one & ~three, two & ~three
            return one

Actually, this approach can be generalized for the case that each number appears 5 times except one:

    class Solution(object):
        def singleNumber(self, nums):
            one = two = three = four = 0
            for x in nums:
                one, two, three, four, five = one ^ x, two | (one & x), three | (two & x), four | (three & x), four & x
                one, two, three, four = one & ~three & ~five, two & ~three, three & ~four, four & ~five
            return one

If each number appears 5 times except that one number appears only 3 times, `return three` will be the result
