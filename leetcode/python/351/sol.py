
Short Hack in Python

https://leetcode.com/problems/android-unlock-patterns/discuss/82542

* Lang:    python3
* Author:  StefanPochmann
* Votes:   9

    def numberOfPatterns(self, m, n, patterns=[]):
        while len(patterns) <= n:
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += sum(not bad(''.join(p))
                            for p in itertools.permutations('123456789', len(patterns))),
        return sum(patterns[m:n+1])

---

A faster version without `itertools`:

    def numberOfPatterns(self, m, n, patterns=[['']]):
        while len(patterns) <= n:
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += [p+d for p in patterns[-1] for d in '123456789'
                         if d not in p and not bad(p+d)],
        return sum(map(len, patterns[m:n+1]))
