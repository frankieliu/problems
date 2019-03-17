
Why this solution is so slow?

https://leetcode.com/problems/first-unique-character-in-a-string/discuss/251963

* Lang:    python3
* Author:  Nimrod0901
* Votes:   0

```Python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list(filter(lambda el: s.count(el) == 1, s))
        return s.find(lst[0]) if lst else -1
```

10000+ms
