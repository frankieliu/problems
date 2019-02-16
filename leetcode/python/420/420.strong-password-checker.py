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
        """
        :type s: str
        :rtype: int
        """
        
