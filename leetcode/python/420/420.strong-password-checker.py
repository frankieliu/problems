#
# @lc app=leetcode id=420 lang=python3
#
# [420] Strong Password Checker
#
# https://leetcode.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (18.20%)
# Total Accepted:    5.8K
# Total Submissions: 31.7K
# Testcase Example:  '""'
#
# A password is considered strong if below conditions are all met:
#
#
# ⁠It has at least 6 characters and at most 20 characters.
# ⁠It must contain at least one lowercase letter, at least one uppercase
# letter, and at least one digit.
# ⁠It must NOT contain three repeating characters in a row ("...aaa..." is
# weak, but "...aa...a..." is strong, assuming other conditions are met).
#
#
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is
# already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one
# change.
#
class Solution:
    def strongPasswordChecker(self, s):
        # one lowercase
        one_lower = False or any('a' <= ch <= 'z' for ch in s)
        one_upper = False or any('A' <= ch <= 'Z' for ch in s)
        one_digit = False or any('0' <= ch <= '9' for ch in s)

        p = 2
        change = 0
        one, two = 0, 0
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:  # three or more repeating
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1
                change += length//3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                p += 1

        missing = 3 - one_lower - one_upper - one_digit

        if len(s) < 6:
            return max(missing, 6-len(s))
        elif len(s) <= 20:
            return max(missing, change)
        else:
            delete = len(s) - 20

            # for length % 3 == 0 just need one delete to reduce change
            # xx(x) single delete reduces
            change -= min(delete, one)

            # for length % 3 == 1 need two deletes to reduce change by 1
            change -= min(max(delete - one, 0), two * 2)//2

            # for remaining deletes, need three deletes to reduce change by 1
            change -= max(delete - one - 2 * two, 0)//3

            return delete + max(missing, change)



test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*0
