
Python solution

https://leetcode.com/problems/additive-number/discuss/75578

* Lang:    python3
* Author:  StefanPochmann
* Votes:   38

Just trying all possibilities for the first two numbers and checking whether the rest fits.

    def isAdditiveNumber(self, num):
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if b != str(int(b)):
                continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False