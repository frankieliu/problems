
Is there something WRONG with the given answer

https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/231878

* Lang:    python3
* Author:  le0192
* Votes:   0

my code is as below:
```
class Solution(object):
    def smallestFromLeaf(self, root):
        if not root:
            return \'\'
        return min(self.smallestFromLeaf(root.left)+chr(root.val + 97), self.smallestFromLeaf(root.right)+chr(root.val + 97))
```
when I submited, I got a wrong answer
Input:
[0,null,1]
Output:
"a"
Expected:
"ba"
who can tell me why
