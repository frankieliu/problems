
Simple Python Solution

https://leetcode.com/problems/counting-bits/discuss/79538

* Lang:    python3
* Author:  startingwars
* Votes:   17

Code works by constantly extending a list with itself but with the values incremented by 1.

    def countBits(self, num):
            """
            :type num: int
            :rtype: List[int]
            """
            
            iniArr = [0]
            if num > 0:
                amountToAdd = 1
                while len(iniArr) < num + 1:
                    iniArr.extend([x+1 for x in iniArr])
            
            return iniArr[0:num+1]

Simple python solution that runs in O(n) time. Let me know if there are any ways to improve it.
