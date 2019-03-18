
Many different ways: 1-liners, 2-liners & Concise 4-liner in Python, 80ms

https://leetcode.com/problems/ransom-note/discuss/85940

* Lang:    python3
* Author:  o_sharp
* Votes:   7

Trivial but the shortest method:
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in ransomNote)
```
Based on the trivial method, we can use ```set``` to avoid some duplication. This works amazingly fast for the test cases. 
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))
```
Or even exploiting the given condition that there are only small letters:
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in string.ascii_lowercase)
```
It gave me 80 ms, the fastest method listed here.

=================================

Ok, here come some more "proper" ways. Proper, as in they don't assume anything about the alphabet.

Proper Method 1: Use Counter and compare letters' counts:
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c1, c2 = collections.Counter(ransomNote), collections.Counter(magazine)
        return all(k in c2 and c2[k]>=c1[k] for k in c1)
```


Proper Method 2: Sort the strings and do a traversal.
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s, i = sorted(ransomNote), 0
        for c in sorted(magazine):
            i += i<len(s) and s[i]==c
        return i==len(s)
```
Longer but easier to understand version. There is an extra check ```c>s1[i]``` for faster termination, but it's not really faster for the test cases here.
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1, s2, i = sorted(ransomNote), sorted(magazine), 0
        for c in s2:
            if i==len(s1) or c>s1[i]:
                break
            if c==s1[i]:
                i += 1
        return i==len(s1)
```
