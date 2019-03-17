
Two simple solutions without recursion or iteration: O(1) time and O(1) space

https://leetcode.com/problems/power-of-three/discuss/77903

* Lang:    python3
* Author:  JavaXu
* Votes:   11

Solution 1:

    class Solution(object):
        def isPowerOfThree(self, n):
            # 1162261467=3^19. 3^20 is bigger than int.
            return n > 0 and 1162261467 % n == 0


Solution 2:


    class Solution(object):
        def isPowerOfThree(self, n):
            # power_list: 3^0, 3^1, ..., 3^19
            power_list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
            return n in power_list
