
1-liner, O(1) space

https://leetcode.com/problems/decode-ways/discuss/30379

* Lang:    python3
* Author:  StefanPochmann
* Votes:   70

[This is the Python](https://xkcd.com/353/).

    def numDecodings(self, s):
        return reduce(lambda(v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1

---

More readable version:

    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w

- `w` tells the number of ways
- `v` tells the previous number of ways
- `d` is the current digit
- `p` is the previous digit
