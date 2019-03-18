
1-liners Python + Ruby

https://leetcode.com/problems/find-the-difference/discuss/86946

* Lang:    python3
* Author:  StefanPochmann
* Votes:   3

**Ruby:**
```
def find_the_difference(s, t)
  (s + t).bytes.reduce(:^).chr
end
```
(previously I had `unpack("c*")` instead of `bytes`, thanks @hbin)

**Python:**

    def findTheDifference(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

    def findTheDifference(self, s, t):
        return chr(reduce(int.__xor__, map(ord, s+t)))
