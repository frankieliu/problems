#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (44.43%)
# Total Accepted:    36.3K
# Total Submissions: 81.8K
# Testcase Example:  '13'
#
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
