
Python with binary search library function instead

https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/110023

* Lang:    python3
* Author:  rtom09
* Votes:   0

Not optimized, but this was my first try.

```
    def nextGreatestLetter(self, letters, target):
        a = bisect.bisect_left(letters, target)
        if a < len(letters) and letters[a] == target:
            a = bisect.bisect_right(letters, target)
        if a >= len(letters):
            a %= len(letters) 
        return letters[a]
```
