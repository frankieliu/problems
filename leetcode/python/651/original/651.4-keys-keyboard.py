#
# @lc app=leetcode id=651 lang=python3
#
# [651] 4 Keys Keyboard
#
# https://leetcode.com/problems/4-keys-keyboard/description/
#
# algorithms
# Medium (50.10%)
# Total Accepted:    11.6K
# Total Submissions: 23.2K
# Testcase Example:  '1'
#
# Imagine you have a special keyboard with the following keys: 
# Key 1: (A):  Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already
# been printed. 
# 
# 
# 
# Now, you can only press the keyboard for N times (with the above four keys),
# find out the maximum numbers of 'A' you can print on screen.
# 
# 
# Example 1:
# 
# Input: N = 3
# Output: 3
# Explanation: 
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
# 
# 
# 
# Example 2:
# 
# Input: N = 7
# Output: 9
# Explanation: 
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
# 
# 
# 
# Note:
# 
# 1 
# Answers will be in the range of 32-bit signed integer.
# 
# 
# 
#
class Solution:
    def maxA(self, N: int) -> int:
        
