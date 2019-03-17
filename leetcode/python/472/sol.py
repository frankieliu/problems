
Very concise 3-liner in Python. A few tricks explained.

https://leetcode.com/problems/concatenated-words/discuss/95693

* Lang:    python3
* Author:  o_sharp
* Votes:   0

And pretty fast, too:
```
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        s = {w for w in words if w}
        f = lambda w:not w or any(w[:i+1] in s and f(w[i+1:]) for i in range(len(w),-1,-1))
        return [w for w in sorted(s,key=len)[::-1] if s.discard(w) or f(w)]
```

A easier to understand version is like this:
```
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret, s = [], {w for w in words if w}
        f = lambda w:not w or any(w[:i+1] in s and f(w[i+1:]) for i in range(len(w),-1,-1))
        for w in sorted(s, key=len, reverse=True):
            s.discard(w)
            if f(w):
                ret.append(w)
        return ret
```

Trick 1: We need to sort the words according to the length. After that, we can safely remove the words one by one from the longest to the shortest in the set because the longer words could never a substring of shorter ones.

This allows us to write very concise code.

Trick 2: ```s.discard(w)	``` always return None, so we can use ```if s.discard(w) or f(w)```. I first saw @StefanPochmann  used this trick elsewhere.

Trick 3: In ```not w or any(w[:i+1] in s and f(w[i+1:]) for i in range(len(w),-1,-1))```, ```not w or``` is similar. This allows us to write a 1-line recursion.
