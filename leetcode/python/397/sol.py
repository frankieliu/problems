
3 Lines Python Recursive AC Solution

https://leetcode.com/problems/integer-replacement/discuss/88053

* Lang:    python3
* Author:  YJL1228
* Votes:   5

```
class Solution(object):
    def integerReplacement(self, n, counter=0):
    	if n == 1: return counter
    	if not n%2: return self.integerReplacement(n/2, counter+1)
    	else: return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))
```
**EDIT:**
Please refer to more improvements by @WKVictor's post under this topic.
