from collections import defaultdict
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nexts = 1
        end_bit = 1<<len(s)
        d = defaultdict(int)
        for i,c in enumerate(s):
            d[c] |= 1<<i
        for c in p:
            if c == '*':
                nexts =  (end_bit<<1) - (nexts & -nexts)
            elif c == '?':
                nexts <<= 1
            else:
                nexts = (nexts & d[c]) << 1
            if nexts == 0:
                return False
        return nexts & end_bit != 0
