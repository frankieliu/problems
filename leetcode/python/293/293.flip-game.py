#
# @lc app=leetcode id=293 lang=python3
#
# [293] Flip Game
#
# https://leetcode.com/problems/flip-game/description/
#
# algorithms
# Easy (58.57%)
# Total Accepted:    39.8K
# Total Submissions: 67.9K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
# 
# Write a function to compute all possible states of the string after one valid
# move.
# 
# Example:
# 
# 
# Input: s = "++++"
# Output: 
# [
# ⁠ "--++",
# ⁠ "+--+",
# ⁠ "++--"
# ]
# 
# 
# Note: If there is no valid move, return an empty list [].
# 
#
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        
