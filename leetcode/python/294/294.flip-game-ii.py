#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#
# https://leetcode.com/problems/flip-game-ii/description/
#
# algorithms
# Medium (47.81%)
# Total Accepted:    41.6K
# Total Submissions: 87K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
# 
# Write a function to determine if the starting player can guarantee a win.
# 
# Example:
# 
# 
# Input: s = "++++"
# Output: true 
# Explanation: The starting player can guarantee a win by flipping the middle
# "++" to become "+--+".
# 
# 
# Follow up:
# Derive your algorithm's runtime complexity.
#
class Solution:
    def canWin(self, s: str) -> bool:
