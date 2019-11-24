#
# @lc app=leetcode id=759 lang=python3
#
# [759] Employee Free Time
#
# https://leetcode.com/problems/employee-free-time/description/
#
# algorithms
# Hard (60.88%)
# Total Accepted:    12.3K
# Total Submissions: 20.2K
# Testcase Example:  '[[[1,2],[5,6]],[[1,3]],[[4,10]]]'
#
#
# We are given a list schedule of employees, which represents the working time
# for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals
# are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free
# time for all employees, also in sorted order.
#
#
# Example 1:
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
#
#
# Example 2:
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
#
#
#
#
# (Even though we are representing Intervals in the form [x, y], the objects
# inside are Intervals, not lists or arrays.  For example, schedule[0][0].start
# = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)
#
# Also, we wouldn't include intervals like [5, 5] in our answer, as they have
# zero length.
#
#
# Note:
# schedule and schedule[i] are lists with lengths in range [1, 50].
# 0 .
#
#
# Definition for an interval.
# class Interval:
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e
import heapq


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)


class Solution:
    """
    Find the empty slot in the employee schedule
    1. priority queue insertion
    2. pull
    """
    def employeeFreeTime(self, schedule):

        h = []
        aset = set(range(len(schedule)))
        for i, emplist in enumerate(schedule):
            heapq.heappush(
                h, (emplist[0].start, emplist[0].end, i, 0, len(emplist)))
        res = []
        curend = None
        while h:
            start, end, empno, intno, intmax = heapq.heappop(h)
            intno_next = intno + 1
            if intno_next < intmax:
                int_next = schedule[empno][intno_next]
                heapq.heappush(
                    h,
                    (int_next.start, int_next.end, empno, intno_next, intmax))
            else:
                aset.remove(empno)
            print(start, end)
            if curend is not None:
                if start > curend:
                    res.append(Interval(curend, start))
                curend = max(curend, end)
            else:
                curend = end

        return res


test = True
if test:
    sol = Solution()
    case = [False] * 1 + [True] + [False] * 2
    if case[0]:
        # Example 1:
        schedule = [[Interval(s=1, e=2),
                     Interval(s=5, e=6)], [Interval(s=1, e=3)],
                    [Interval(s=4, e=10)]]
        # Output: [[3,4]]
        print(sol.employeeFreeTime(schedule))
    if case[1]:
        # Example 2:
        testcase = [[{
            "$id": "1",
            "start": 7,
            "end": 24
        }, {
            "$id": "2",
            "start": 29,
            "end": 33
        }, {
            "$id": "3",
            "start": 45,
            "end": 57
        }, {
            "$id": "4",
            "start": 66,
            "end": 69
        }, {
            "$id": "5",
            "start": 94,
            "end": 99
        }],
                    [{
                        "$id": "6",
                        "start": 6,
                        "end": 24
                    }, {
                        "$id": "7",
                        "start": 43,
                        "end": 49
                    }, {
                        "$id": "8",
                        "start": 56,
                        "end": 59
                    }, {
                        "$id": "9",
                        "start": 61,
                        "end": 75
                    }, {
                        "$id": "10",
                        "start": 80,
                        "end": 81
                    }],
                    [{
                        "$id": "11",
                        "start": 5,
                        "end": 16
                    }, {
                        "$id": "12",
                        "start": 18,
                        "end": 26
                    }, {
                        "$id": "13",
                        "start": 33,
                        "end": 36
                    }, {
                        "$id": "14",
                        "start": 39,
                        "end": 57
                    }, {
                        "$id": "15",
                        "start": 65,
                        "end": 74
                    }],
                    [{
                        "$id": "16",
                        "start": 9,
                        "end": 16
                    }, {
                        "$id": "17",
                        "start": 27,
                        "end": 35
                    }, {
                        "$id": "18",
                        "start": 40,
                        "end": 55
                    }, {
                        "$id": "19",
                        "start": 68,
                        "end": 71
                    }, {
                        "$id": "20",
                        "start": 78,
                        "end": 81
                    }],
                    [{
                        "$id": "21",
                        "start": 0,
                        "end": 25
                    }, {
                        "$id": "22",
                        "start": 29,
                        "end": 31
                    }, {
                        "$id": "23",
                        "start": 40,
                        "end": 47
                    }, {
                        "$id": "24",
                        "start": 57,
                        "end": 87
                    }, {
                        "$id": "25",
                        "start": 91,
                        "end": 94
                    }]]
        int_list = []
        for alist in testcase:
            int_list.append(
                list(map(lambda x: Interval(x["start"], x["end"]), alist)))
        # print(int_list)
        # answer:
        # [{"$id":"1","end":18,"start":16},{"$id":"2","end":27,"start":26},{"$id":"3","end":39,"start":36},{"$id":"4","end":78,"start":71},{"$id":"5","end":91,"start":81}]
        # expected_answer:
        # [{"$id":"1","end":27,"start":26},{"$id":"2","end":39,"start":36},{"$id":"3","end":91,"start":87}]

        schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        # Output: [[5,6],[7,9]]
        print(sol.employeeFreeTime(int_list))
