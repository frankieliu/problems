
7-liner in Python, One Pass

https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/91225

* Lang:    python3
* Author:  o_sharp
* Votes:   0

Unique identifiers exist if we check all 10 digits in this order```[0, 2, 4, 6, 8, 1, 3, 5, 7, 9]```.
```
class Solution(object):
    def originalDigits(self, s):
        l, cnt, ret = [('zero','z'),('one','o'),('two','w'),('three','h'),('four','u'),('five','f'),('six','x'),('seven','s'),('eight','g'),('nine','i')], collections.Counter(s), []
        for i in [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]:
            n = cnt[l[i][1]]
            for c in l[i][0]:
                cnt[c] -= n
            ret += [str(i)]*n
        return ''.join(sorted(ret))
```
