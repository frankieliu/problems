#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (30.45%)
# Total Accepted:    127.2K
# Total Submissions: 417.7K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
