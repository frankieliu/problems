#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (48.22%)
# Total Accepted:    47K
# Total Submissions: 97.4K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the
# sequence:
#
#
# "abc" -> "bcd" -> ... -> "xyz"
#
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
#
# Example:
#
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]


from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        h = defaultdict(list)
        for s in strings:
            y = [ord(x) for x in s]
            z = tuple([(x - y[0]) % 26 for x in y])
            h[z].append(s)
        return [x for x in h.values()]


test = True
if test:
    s = Solution()
    Input = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    # Output:
    # [
    # ⁠ ["abc","bcd","xyz"],
    # ⁠ ["az","ba"],
    # ⁠ ["acef"],
    # ⁠ ["a","z"]
    # ]

    print(s.groupStrings(Input))
