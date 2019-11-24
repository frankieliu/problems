#
# @lc app=leetcode id=828 lang=python3
#
# [828] Unique Letter String
#
# https://leetcode.com/problems/unique-letter-string/description/
#
# algorithms
# Hard (38.03%)
# Total Accepted:    4.1K
# Total Submissions: 10.7K
# Testcase Example:  '"ABC"'
#
# A character is unique in string S if it occurs exactly once in it.
#
# For example, in string S = "LETTER", the only unique characters are "L" and
# "R".
#
# Let's define UNIQ(S) as the number of unique characters in string S.
#
# For example, UNIQ("LETTER") =  2.
#
# Given a string S with only uppercases, calculate the sum of UNIQ(substring)
# over all non-empty substrings of S.
#
# If there are two or more equal substrings at different positions in S, we
# consider them different.
#
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
#
#
#
# Example 1:
#
#
# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#
# Example 2:
#
#
# Input: "ABA"
# Output: 8
# Explanation: The same as example 1, except uni("ABA") = 1.
#
#
#
#
# Note: 0 <= S.length <= 10000.
#
#

from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s):
        """
        The key idea is to separate U in U_c i.e. calculate the # of unique
        substrings containing 'c'

        U(x) = sum_{c \in A} U_c(x) where A is your alphabet

        1. create a map of character to the index of that character
           for example LETTER
           m['E'] = [1,4]

        2. add sentinels
           [-1,1,4,6]

        3. multiply
           [-1 -> 1] * [2 -> 4]
        """
        # create a mat
        m = defaultdict(list)
        for i in range(len(s)):
            m[s[i]].append(i)

        sum = 0
        for k,v in m.items():
            A = [-1] + v + [len(s)]
            for i in range(1, len(A)-1):
                sum += (A[i]-A[i-1])*(A[i+1]-A[i])
        return sum % (10**9 + 7)


test = True
if test:
    s = Solution()
    case = [False, True, False]
    if case[0]:
        print(s.uniqueLetterString("LETTER"))
    if case[1]:
        print(s.uniqueLetterString("ABC"))
