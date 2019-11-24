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
        a = [(str(i), 1) for i in range(0,256)]
        dp = {}
        for x in a:
            dp[(x[0],x[1])] = [x[0]]

        def helper(a,n):  # i is the ith index, n is the number left
            # print(a, n)
            if n == 1 and (a,n) not in dp:
                return []

            if (a,n) in dp:
                return dp[(a,n)]

            res = []
            # choose one digit a[0]
            if 1*(n-1) <= (len(a)-1) <= 3*(n-1):
                ans = helper(a[1:], n-1)
                if ans:
                    res = [a[0]+'.'+x for x in ans]

            # choose two number
            if len(a) > 2 and 1*(n-1) <= (len(a)-2) <= 3*(n-1):
                # print("a:{} a[0:1]:{}".format(a,a[0:1]))
                if int(a[0:2]) > 9:
                    ans = helper(a[2:], n-1)
                    if ans:
                        res += [a[0:2]+'.'+x for x in ans]

            # choose three number
            if len(a) > 3 and 1*(n-1) <= (len(a)-3) <= 3*(n-1):
                if int(a[0:3]) > 99:
                    ans = helper(a[3:], n-1)
                    if ans:
                        res += [a[0:3]+'.'+x for x in ans]

            dp[(a,n)] = res
            return res
        return helper(s,4)


test = True
if test:
    s = Solution()
    # print(s.restoreIpAddresses('25525511135'))
    print(s.restoreIpAddresses('010010'))     # ["0.10.0.10","0.100.1.0"]
