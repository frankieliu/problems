
Python solution (linear time, constant space) with explanation

https://leetcode.com/problems/construct-the-rectangle/discuss/97230

* Lang:    python3
* Author:  laser
* Votes:   5

    import math
    class Solution(object):
        # based on area input, linear time, and constant space complexity
        def constructRectangle(self, area):
            # to meet the requirements of point 3, getting closest to the center,
            # the square root will get as close as the center as possible
            mid = int(math.sqrt(area))

            # consider mid to be W here, and until you get to a point where there
            # are exact integers that will equate to a rectangle with area, subtract from mid/W
            # because point 2 states that L >= W
            while area % mid != 0:
                mid -= 1
        
            # compute L from W (mid), and W (mid)
            return [int(area/mid),mid]
