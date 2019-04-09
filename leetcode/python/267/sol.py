
4 lines Python solution

https://leetcode.com/problems/palindrome-permutation-ii/discuss/69691

* Lang:    python3
* Author:  xcv58
* Votes:   8

Use `collections.Counter` and `itertools.permutations`

    class Solution(object):
        def generatePalindromes(self, s):
            d = collections.Counter(s)
            m = tuple(k for k, v in d.iteritems() if v % 2)
            p = ''.join(k*(v/2) for k, v in d.iteritems())
            return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else []
