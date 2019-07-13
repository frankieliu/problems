#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (31.75%)
# Total Accepted:    51.5K
# Total Submissions: 162.2K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
# Example 1:
#
#
# Input: "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: "cbacdcbc"
# Output: "acdb"
#
#
class Solution:
    def removeDuplicateLetters(self, s):
        """
        Main idea:
        1. keep adding a letter to the result if not present in result
        2. while letter added is
           1. lexicographically smaller than letter at tail of result AND
           2. tail of result can be found latter in s, then
           3. it is safe to remove tail
        """
        # keeps track of the last index of a letter
        rindex = {c: i for i, c in enumerate(s)}
        used = {c: False for c in rindex.keys()}

        res = rindex.keys()
        j = 0  # index into result
        for i, c in enumerate(s):
            if not used[c]:
                while j > 0 and c < res[j - 1] and i < rindex[res[j - 1]]:
                    used[res[j - 1]] = False
                    j -= 1
                used[c] = True
                res[j] = c
                j += 1

        return "".join(res[0:j])


test = True
if test:
    s = Solution()
    case = [False] * 0 + [True] + [False] * 2
    if case[0]:
        # Example 1:
        Input = "bcabc"
        # Output: "abc"
        print(s.removeDuplicateLetters(Input))
    if case[1]:
        # Example 2:
        Input = "cbacdcbc"
        # Output: "acdb"
        print(s.removeDuplicateLetters(Input))
