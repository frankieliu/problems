
Clean O(n) Python Solution

https://leetcode.com/problems/gas-station/discuss/42680

* Lang:    python3
* Author:  briankwong
* Votes:   3

    class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            start = rest = overall = 0
            for i in xrange(len(gas)):
                rest += gas[i] - cost[i]
                overall += gas[i] - cost[i]
                if rest < 0:
                    rest, start = 0, i + 1
            return start if overall >=0 else -1
