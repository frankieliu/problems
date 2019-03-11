#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (26.68%)
# Total Accepted:    31.6K
# Total Submissions: 118.2K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally.
#
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
#
#
# Example
#
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
#
# Output:
# false
#
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#
#
#
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        """Corner Case:

        sum(pick values) < desired sum: The first player never wins.

        sum(pick values) == desired sum: Whoever takes the last
        wins. (Irrelevant to who pick which number first)

        max choosable number > desired sum: The first player always
        wins by picking the max number.


        Code Supplemental Explanation:
        -----------------------------
        Record: Used to rememeber win\loss for current state. (what
                numbers have been picked, True: Win, False: Lose)

        Bitmap: Record which number has been picked. Also used as an
                index to access the win loss record. (if in hash
                table)

        Win if there is a way of picking a number 'n' such that no
        matter how opponent picks next, the opponent lose.

        Lose if there is no way of picking a number 'n' that satisfies
        the above situation.

        Win\Loss is for the first player with the game status (bitmap
        passed in).

        """

        max_sum = maxChoosableInteger*(maxChoosableInteger+1)//2

        if max_sum < desiredTotal:
            return False

        elif max_sum == desiredTotal:
            return (maxChoosableInteger % 2 == 1)

        if maxChoosableInteger >= desiredTotal:
            return True

        bit_mask = 1 << maxChoosableInteger  # bit 0: unused, bit 1: used

        self.record = {}

        return self.checkWin(maxChoosableInteger, bit_mask, desiredTotal)


    def checkWin(self, max_num, bit_mask, remain_sum):

        if bit_mask in self.record:
            return self.record[bit_mask]

        for i in range(max_num):

            if (1 & (bit_mask >> i)) != 0:
                # skip already-picked number
                continue

            n = i + 1  # n: picked number
            if (n >= remain_sum) or (self.checkWin(max_num, bit_mask | (1<< i), remain_sum-n) is False):
                self.record[bit_mask] = True
                return True

        self.record[bit_mask] = False
        return False
