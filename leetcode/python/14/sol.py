
5 line python with zip() and len(set())

https://leetcode.com/problems/longest-common-prefix/discuss/7138

* Lang:    python3
* Author:  zcjsword
* Votes:   17

Just for fun :)

    class Solution(object):
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]; rtype: str
            """
            sz, ret = zip(*strs), ""
            # looping corrected based on @StefanPochmann's comment below
            for c in sz:
                if len(set(c)) > 1: break
                ret += c[0]
            return ret
