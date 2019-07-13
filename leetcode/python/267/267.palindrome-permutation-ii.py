#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (33.28%)
# Total Accepted:    24.8K
# Total Submissions: 74.4K
# Testcase Example:  '"aabb"'
#
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
#
# Example 1:
#
#
# Input: "aabb"
# Output: ["abba", "baab"]
#
# Example 2:
#
#
# Input: "abc"
# Output: []
#
#
class Solution:
    def generatePalindromes(self, s):

        def perm(s, i):
            out = []
            if i == (len(s)-1):
                return [s[i]]
            for k in range(i, len(s)):
                if k > i and s[k] in s[i:k]:
                    continue
                s[i], s[k] = s[k], s[i]
                out += ["".join([s[i], x]) for x in perm(s, i+1)]
                s[i], s[k] = s[k], s[i]
            return out

        if len(s) == 0:
            return []

        if len(s) == 1:
            return [s]

        s = sorted(list(s))

        odd = (len(s) % 2) == 1

        theOne = None
        pair = []
        i = 0
        while i < len(s)-1:
            if s[i+1] != s[i]:
                if odd:
                    if theOne is None:
                        theOne = s[i]
                        i += 1
                        continue
                    else:
                        # found another unique one
                        return []
                else:
                    # even and no match
                    # print("even and no match", s[i], s[i+1])
                    return []
            pair.append(s[i])
            i += 2

        if odd and i == len(s)-1:
            theOne = s[i]

        if theOne is None:
            mid = ""
        else:
            mid = theOne

        return [x + mid + x[::-1] for x in perm(list(pair), 0)]


test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        Input = "aabbc"
        # Output: ["abba", "baab"]
        print(s.generatePalindromes(Input))
    if case[1]:
        # Input: "aaaabbbbcccc"
        # Output: []
        print(s.generatePalindromes(Input))
