#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (31.50%)
# Total Accepted:    71.8K
# Total Submissions: 228K
# Testcase Example:  '"ab"\n"acb"'
#
# Given two strings s and t, determine if they are both one edit distance
# apart.
#
# Note: 
#
# There are 3 possiblities to satisify one edit distance apart:
#
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
#
#
# Example 1:
#
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
#
#
# Example 2:
#
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
#
# Example 3:
#
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
#
#
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def _isOne(s, t, si, ti, edits):
            if ti == len(t) and si == len(s):
                if edits == 1:
                    return False
                else:
                    return True
            if edits == 0 and (ti == len(t) or si == len(s)):
                return False
            if ti < len(t) and si < len(s) and s[si] == t[ti]:
                return _isOne(s, t, si+1, ti+1, edits)
            else:
                if edits == 0:
                    return False
                if len(s) == len(t):
                    return _isOne(s, t, si+1, ti+1, edits-1)
                if len(s) > len(t):
                    return _isOne(s, t, si+1, ti, edits-1)
                else:
                    return _isOne(s, t, si, ti+1, edits-1)
        if len(s) == 0 and len(t) == 0:
            return False
        return _isOne(s, t, 0, 0, 1)


test = True
if test:
    # Input:
    s = "1203"
    t = "1213"
    s = "a"
    t = ""

    sln = Solution()
    print(sln.isOneEditDistance(s, t))
