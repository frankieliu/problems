#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (42.77%)
# Total Accepted:    21.8K
# Total Submissions: 50.9K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
# 
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
# ..., then the summary will be:
# 
# 
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
# 
# 
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are
# small compared to the data stream's size?
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
