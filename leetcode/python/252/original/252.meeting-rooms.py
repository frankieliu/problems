#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (51.51%)
# Total Accepted:    76.9K
# Total Submissions: 149.2K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
# 
# Example 1:
# 
# 
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# 
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: true
# 
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
