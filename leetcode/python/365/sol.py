
Python solution gcd

https://leetcode.com/problems/water-and-jug-problem/discuss/83711

* Lang:    python3
* Author:  hliu94
* Votes:   10

    class Solution(object):
        def canMeasureWater(self, x, y, z):
            """
            :type x: int
            :type y: int
            :type z: int
            :rtype: bool
            """
            a,b=x,y
            while y:
                r=x%y
                x=y
                y=r
            return bool(not z or (x and z<=a+b and not z%x))
