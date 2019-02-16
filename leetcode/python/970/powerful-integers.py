"""970. Powerful Integers
Virtual User Accepted: 0
Virtual User Tried: 0
Virtual Total Accepted: 0
Virtual Total Submissions: 0
Difficulty: Easy

Given two non-negative integers x and y, an integer is powerful if it
is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or
equal to bound.

You may return the answer in any order.  In your answer, each value
should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6

"""

from math import log

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if (bound == 0):
            return []

        out = set()
        if x == 1:
            nx = 0
        else:
            nx = int(log(bound)/log(x))
        xpart = 1
        for i in range(0, nx+1):
            diff = bound - xpart
            if diff == 0:
                continue
            if y == 1:
                ny = 0
            else:
                ny = int(log(diff)/log(y))
            ypart = 1
            for j in range(0, ny+1):
                # print(xpart, ypart, xpart+ypart)
                out.add(xpart + ypart)
                ypart *= y
            xpart *= x
        return list(out)


s = Solution()
print(s.powerfulIntegers(2, 3, 10))
print(s.powerfulIntegers(3, 5, 15))
print(s.powerfulIntegers(2, 2, 3))
