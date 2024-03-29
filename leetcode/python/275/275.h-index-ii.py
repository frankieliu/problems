#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (35.13%)
# Total Accepted:    74.9K
# Total Submissions: 213.1K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
#
# Example:
#
#
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had
# ⁠            received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining
# two with no more than 3 citations each, her h-index is 3.
#
# Note:
#
# If there are several possible values for h, the maximum one is taken as the
# h-index.
#
# Follow up:
#
#
# This is a follow up problem to H-Index, where citations is now guaranteed to
# be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
#
#
#


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        def bl(a):
            i, j = 0, len(a)
            while i < j:

                mid = (i + j) // 2
                if a[mid] < (len(a) - mid):
                    # print(a[mid], mid, "right")
                    i = mid + 1
                else:
                    # print(a[mid], mid, "left")
                    j = mid
            return i

        """
        like bisect left, but the target
        keeps changing to the index being looked at
        """
        return len(citations) - bl(citations)


test = True
if test:
    s = Solution()
    case = [False, False, False, False, False, True, False]
    if case[0]:

        # Input: citations = [0,1,3,5,6]
        # Output: 3
        # Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
        # of them had
        # ⁠            received 0, 1, 3, 5, 6 citations respectively.
        # Since the researcher has 3 papers with at least 3 citations each and the
        # remaining
        # two with no more than 3 citations each, her h-index is 3.

        citations = [0, 1, 3, 5, 6]
        print(s.hIndex(citations))
    if case[1]:
        citations = [8, 8, 8, 8, 8]
        print(s.hIndex(citations))
    if case[2]:
        citations = [0, 0, 0, 0, 0]
        print(s.hIndex(citations))
    if case[3]:
        citations = [2, 2, 2, 2, 2]
        print(s.hIndex(citations))
    if case[4]:
        citations = []
        print(s.hIndex(citations))
    if case[5]:
        citations = [3]
        print(s.hIndex(citations))
