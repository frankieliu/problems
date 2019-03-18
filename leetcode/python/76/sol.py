
12 lines Python

https://leetcode.com/problems/minimum-window-substring/discuss/26804

* Lang:    python3
* Author:  StefanPochmann
* Votes:   138

The current window is `s[i:j]` and the result window is `s[I:J]`. In `need[c]` I store how many times I need character `c` (can be negative) and `missing` tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result.

    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
