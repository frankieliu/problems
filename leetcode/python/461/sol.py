
Python bitwise operation beat 100%

https://leetcode.com/problems/hamming-distance/discuss/94864

* Lang:    python3
* Author:  superonion
* Votes:   0

```
xor = x ^ y
count = 0
while xor > 0:
    if xor & 1:
        count += 1
    xor = xor >> 1
return count
```
