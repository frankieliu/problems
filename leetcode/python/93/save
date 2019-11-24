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
from collections import deque

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # ip address must have 4 possible numbers
        # make into a dp problem

        dp = [0] * 5
        for i in range(0, 5):
            dp[i] = [0] * (len(s)+1)
        dp[4][len(s)] = 1

        for p in range(len(s)-1, -1, -1):
            for c in range(3, -1, -1):

                out = 0
                if (p+1) <= len(s):
                    print("1", int(s[p:p+1]))
                    out += dp[c+1][p+1]
                if (p+2) <= len(s) and 10 <= int(s[p:p+2]) <= 99:
                    print("2", int(s[p:p+2]))
                    out += dp[c+1][p+2]
                if (p+3) <= len(s) and 100 <= int(s[p:p+3]) < 256:
                    print("3", int(s[p:p+3]))
                    out += dp[c+1][p+3]
                dp[c][p] = out

        # from dp figure out what was taken
        # return dp[0][0]

        st = deque()
        # do a dfs

        out = []
        cur = []
        st.append([0, 0, []])
        while st:
            c, p, cur = st.pop()
            if c == 4 and p == len(s):
                out.append(cur)
            if (c+1) <= 4:
                if (p+1) <= len(s) and dp[c+1][p+1] > 0:
                    tmp = cur[:]
                    tmp.append(int(s[p:p+1]))
                    st.append(
                        [c+1, p+1, tmp])
                if ((p+2) <= len(s) and
                    dp[c+1][p+2] > 0 and
                    10 <= int(s[p:p+2]) <= 99):
                    tmp = cur[:]
                    tmp.append(int(s[p:p+2]))
                    st.append(
                        [c+1, p+2, tmp])
                if ((p+3) <= len(s) and
                    dp[c+1][p+3] > 0 and
                    100 <= int(s[p:p+3]) <= 255):
                    tmp = cur[:]
                    tmp.append(int(s[p:p+3]))
                    st.append(
                        [c+1, p+3, tmp])

            def toString(a):
                return [str(x) for x in a]

        return [".".join(toString(x)) for x in out]


test = False
if test:
    s = Solution()
    # print(s.restoreIpAddresses('25525511135'))
    print(s.restoreIpAddresses('010010'))     # ["0.10.0.10","0.100.1.0"]
