
No loop/recursion, O(1) runtime, just one line python code

https://leetcode.com/problems/add-digits/discuss/68732

* Lang:    python3
* Author:  lime66
* Votes:   12

    class Solution(object):
        def addDigits(self, num):
            return num if num == 0 else num % 9 or 9
