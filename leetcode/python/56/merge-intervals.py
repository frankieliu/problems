"""56. Merge Intervals
Medium

1580

119

Favorite

Share
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Accepted
285,240
Submissions
831,910"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        ints = [[x.start, x.end] for x in intervals]
        s = sorted(ints)

        out = []
        cur = s[0]
        for x in s[1::]:
            if x[0] <= cur[1]:
                cur[1] = max(x[1], cur[1])
            else:
                out.append(cur)
                cur = x
        out.append(cur)
        return out


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
