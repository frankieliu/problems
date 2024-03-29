#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (43.98%)
# Total Accepted:    68K
# Total Submissions: 154.5K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks. Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
#
#
#
# Example:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
#
#
# Note:
#
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
#
#
#
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 1:
            return 1
        c = Counter(tasks)
        hq = [(-y,x) for x,y in c.items()]
        heapq.heapify(hq)
        dq = deque()
        res = []
        idle = 0
        while dq or hq:
            if len(hq) > 0:
                count, x = heapq.heappop(hq)
                count += 1
                dq.append((count, x))
                res.append(x)
            else:
                idle += 1
                if idle == n+1:
                    break
                dq.append((0, '#'))
                res.append("#")
            # print(res, dq)
            if len(dq) > n:
                count, x = dq.popleft()
                # print("poping",(count,x))
                if x == '#':
                    idle -= 1
                if -count > 0:
                    heapq.heappush(hq,(count, x))
        for i in range(len(res)-1,0,-1):
            if res[i] != '#':
                break
        return i+1


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        tasks = ["A","A","A","B","B","B"]
        n = 50
        # Output: 8
        print(sol.leastInterval(tasks, n))
