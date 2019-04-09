
1+7 lines Python (length prefixes)

https://leetcode.com/problems/encode-and-decode-strings/discuss/70448

* Lang:    python3
* Author:  StefanPochmann
* Votes:   33

    class Codec:
    
        def encode(self, strs):
            return ''.join('%d:' % len(s) + s for s in strs)
    
        def decode(self, s):
            strs = []
            i = 0
            while i < len(s):
                j = s.find(':', i)
                i = j + 1 + int(s[i:j])
                strs.append(s[j+1:i])
            return strs
