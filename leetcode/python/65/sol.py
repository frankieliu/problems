
Easy Python Solution 68 ms beats 100%

https://leetcode.com/problems/valid-number/discuss/23739

* Lang:    python3
* Author:  tejas7
* Votes:   25

def isNumber(self, s):

    try: float(s)
    except ValueError: return False
    else: return True

Easy Peasy :)
