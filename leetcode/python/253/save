#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (42.36%)
# Total Accepted:    133.7K
# Total Submissions: 315.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from itertools import chain


class Solution:
    def minMeetingRooms(self, intervals):
        # sort all beginning and end times together
        # whenever we get a begin we either use a new room
        # or a room that has been vacated
        # whenever we get an end we vacate a room

        # we want ends to come first so using 'a'
        t0 = sorted(
            chain(
                *[[[x.start, 'b'], [x.end, 'a']] for x in intervals]))

        vacant = 0
        rooms = 0
        for t in t0:
            if t[1] == 'b':
                if vacant == 0:
                    # take a room
                    rooms += 1
                else:
                    vacant -= 1
            else:  # t[1] == 'e'
                vacant += 1
        return rooms


test = True
if test:
    s = Solution()
    Example = [[0, 30], [5, 10], [15, 20]]
    print(s.minMeetingRooms(Example))
