#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Medium (38.33%)
# Total Accepted:    87.3K
# Total Submissions: 227.7K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
#
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
#
# Please note that both secret number and friend's guess may contain duplicate
# digits.
#
# Example 1:
#
#
# Input: secret = "1807", guess = "7810"
#
# Output: "1A3B"
#
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
#
# Example 2:
#
#
# Input: secret = "1123", guess = "0111"
#
# Output: "1A1B"
#
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
#
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count = defaultdict(int)
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                if count[guess[i]] > 0:
                    cows += 1
                if count[secret[i]] > 0:
                    cows += 1
                count[secret[i]] += 1
                count[guess[i]] -= 1
        return "{}A{}B".format(bulls, cows)


test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        print(s.getHint())
    if case[1]:
        print(s.getHint())
