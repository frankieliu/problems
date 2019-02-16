"""91. Decode Ways
Medium

1107

1316

Favorite

Share

A message containing letters from A-Z is being encoded to numbers
using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total
number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Accepted
229,332
Submissions
1,059,197
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        if int(s[n-1]) != 0:
            dp[n-1] = 1
        for i in range(n-2, -1, -1):
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            elif int(s[i]) != 0:
                dp[i] = dp[i+1]
            else:
                dp[i] = 0

        return dp[0]


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("0"))
print(s.numDecodings("01"))
