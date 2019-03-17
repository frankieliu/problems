
My Python Solution

https://leetcode.com/problems/happy-number/discuss/56915

* Lang:    python3
* Author:  zyt6217315a
* Votes:   72

    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
