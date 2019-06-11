#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.36%)
# Total Accepted:    115.5K
# Total Submissions: 336.2K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
#
# Example:
#
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had
# ⁠            received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining
# two with no more than 3 citations each, her h-index is 3.
#
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
#
#


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0] * (N + 1)
        for el in citations:
            if el > N:
                count[N] += 1
            else:
                count[el] += 1
        print(count)
        s = 0
        for i in range(len(count)-1, -1, -1):
            s += count[i]
            if s >= i:
                break
        return i


test = True
if test:
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    print(s.hIndex(citations))
