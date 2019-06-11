#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (34.49%)
# Total Accepted:    293.8K
# Total Submissions: 851.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intersect(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        a = sorted(intervals)
        last = [x[1] for x in a]
        a.append([max(last)+1, max(last)+1])

        left, right = a[0]
        out = []
        for i in range(1, len(a)):
            nl, nr = a[i]
            # intersection is happening
            if nl <= right:
                if nr <= right:
                    out.append([nl, nr])
                else:
                    if nl != right:
                        out.append([nl, right])
                    right = nr
            else:
                left = nl
                right = nr
        return out

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        a = sorted(intervals)
        last = [x[1] for x in a]
        a.append([max(last)+1, max(last)+1])

        left, right = a[0]
        out = []
        for i in range(1, len(a)):
            nl, nr = a[i]
            if nl <= right:
                if nr <= right:
                    continue
                else:
                    right = nr
            else:
                out.append([left, right])
                left = nl
                right = nr
        return out


test = True
if test:
    s = Solution()
    case=[0, 1]
    if case[0]:
        Input = [[1,3],[2,6],[8,10],[15,18]]
        # Output = [[1,6],[8,10],[15,18]]
        print(s.merge(Input))
    if case[1]:
        Input = [[1, 10], [2, 6], [9, 12], [14, 16], [16, 17]]
        # union [[1, 12], [14, 17]]
        # intersection: [[2, 6], [9, 10]]
        print(s.merge(s.intersect(Input)))
        # note need to merge the output
