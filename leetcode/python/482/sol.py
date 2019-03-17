
10 line simple python solution

https://leetcode.com/problems/license-key-formatting/discuss/96557

* Lang:    python3
* Author:  rtom09
* Votes:   0

```
    def licenseKeyFormatting(self, S, K):
        x = 0
        S = S.replace("-", "").upper()
        mod = len(S) % K
        if mod == 0:
            mod += K
        while mod < len(S):
            S = S[:mod] + "-" + S[mod:]
            mod += K + 1
        return S
```
