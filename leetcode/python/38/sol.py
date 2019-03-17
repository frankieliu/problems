
4-5 lines Python solutions

https://leetcode.com/problems/count-and-say/discuss/15999

* Lang:    python3
* Author:  StefanPochmann
* Votes:   87

**Solution 1** ... using a regular expression

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

---

**Solution 2** ... using a regular expression

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\\2*)', s))
        return s

---

**Solution 3** ... using `groupby`

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s
