
Python-new solution-remainder=integer

https://leetcode.com/problems/sum-of-square-numbers/discuss/104945

* Lang:    python3
* Author:  siyu14
* Votes:   0

class Solution(object):
    def judgeSquareSum(self, c):
        for i in range(0, int(c**(0.5))+1):
#use %1 to check if the result is integer
            if(((c-i*i)**(0.5))%1==0):
                return True
        return False
