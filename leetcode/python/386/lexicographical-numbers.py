"""386. Lexicographical Numbers
Virtual User Accepted: 0
Virtual User Tried: 0
Virtual Total Accepted: 0
Virtual Total Submissions: 0
Difficulty: Medium
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input
size may be as large as 5,000,000.
"""

from math import *

class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        example:
        425
        1
        10 - 19
        100 - 199
        1000 - 1999

        incorrect
        10
        100
        1000
        11
        110
        1100
        111
        1110
        1111

        fill
        10
        100
        1000 - 1009
        101
        1010 - 1019
        102

        rule:
        fill first spot with 1
        keep filling spots with 0 until you can't
        10
        100

        fill next spot with 1
        1--
        10-
        100


        1--
        10-
        100
        101 - 109
        11-
        110
        111 - 119
        12-
        120
        121
        ...
        2--
        20-
        200




        for the last spot must go from 0 to 9
        then fill

        fill first slot from 1-9







        20 - 29
        200
        2000
        30
        300
        3000

        Figure out closest 400
        """

        if n == 0:
            return [0]

        pow = int(log(n)/log(10))

        # Because of funny rounding errors
        if 10**(pow+1) == n:
            pow = pow + 1

        ind = int(n/10**pow)

        # print("pow ind", pow, ind)
        out = []
        for j in range(1, 10):
            # print("Doing", j)
            for p in range(0, pow+1):
                # print(" Power", p)
                if p == pow and j >= ind:
                    endi = n + 1
                else:
                    endi = (j+1) * 10**p

                for i in range(j * 10**p, endi):
                    # print("  Adding", i)
                    out.append(i)
        return out

s = Solution()
print(s.lexicalOrder(1000))

if False:
    for i in range(0, 10000):
        if len(s.lexicalOrder(i)) != i:
            print(i)
