#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (32.60%)
# Total Accepted:    21K
# Total Submissions: 64.5K
# Testcase Example:  '"aabbcc"\n3'
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
#
# Example 1:
#
#
#
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
#
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.
#
#
#
# Example 3:
#
#
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
#
#
#
#
#
from collections import deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        print(s,k)
        pq = [(-s.count(ch), ch) for ch in set(s)]
        heapq.heapify(pq)
        dq = deque()
        res = ""
        print(pq)
        while pq:
            count, ch = heapq.heappop(pq)
            res += ch
            dq.append((count + 1, ch))
            print(dq)
            if len(dq) < k:
                continue
            count, ch = dq.popleft()
            if count:
                heapq.heappush(pq, (count, ch))
        return res if len(res) == len(s) else ""


test = True
if test:
    sol = Solution()
    case = [False] * 3 + [True] + [False] * 3
    if case[0]:
        # Example 1:
        s = "aabbcc"
        k = 3
        # Output: "abcabc"
        print(sol.rearrangeString(s, k))
    if case[1]:
        print("Case 1")
        # Example 2:
        s = "aaabc"
        k = 3
        # Output: ""
        print(sol.rearrangeString(s, k))
    if case[2]:
        # Example 3:
        s = "aaadbbcc"
        k = 2
        # Output: "abacabcd"
        print(sol.rearrangeString(s, k))
    if case[3]:
        # Example 3:
        s = "aaaaaabbbccc"
        k = 4
        # Output: "abacabcd"
        print(sol.rearrangeString(s, k))
