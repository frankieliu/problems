
Some Python solutions

https://leetcode.com/problems/remove-duplicate-letters/discuss/76787

* Lang:    python3
* Author:  StefanPochmann
* Votes:   43

Solutions inspired by those of others. Simpler but less efficient (all still get accepted, of course, in about 50 to 100 ms, normal for Python).

---

**Solution 1**

Inspired by [lixx2100's explanation](https://leetcode.com/discuss/73761/a-short-o-n-recursive-greedy-solution).

    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

---

**Solution 2**

Inspired by [WHJ425's explanation](https://leetcode.com/discuss/73777/easy-to-understand-iterative-java-solution).

    def removeDuplicateLetters(self, s):
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result

---

**Solution 3**

Inspired by [halibut735's solution](https://leetcode.com/discuss/73824/short-16ms-solution-using-stack-which-can-optimized-down-4ms).

    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result
