#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.09%)
# Total Accepted:    285.5K
# Total Submissions: 647.6K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
#
#
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s = [list(x) for x in strs]
        d = defaultdict(list)
        for el in s:
            d["".join(sorted(el))].append(el)
        return [["".join(x) for x in el[1]] for el in d.items()]



test = False
if test:
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams(["eat"]))
    print(s.groupAnagrams([]))
