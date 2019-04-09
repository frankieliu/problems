
Python solution using set (36ms)

https://leetcode.com/problems/missing-ranges/discuss/50623

* Lang:    python3
* Author:  LordCHTsai
* Votes:   3

    class Solution(object):
        def findMissingRanges(self, nums, lower, upper):
            """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: List[str]
            """
            start = [lower] + sorted(set(map(lambda x: x+1, nums)) - set(nums))
            end = sorted(set(map(lambda x: x-1, nums)) - set(nums)) + [upper]
            ret = []
            for s, e in zip(start, end):
                if s < e:
                    ret.append('{}->{}'.format(s, e))
                elif s == e:
                    ret.append('{}'.format(s))
            return ret

Increase numbers by 1 to find all the starts and decrease numbers by 1 to find all the ends. Then add lower and upper boundaries to starts and ends. If start < end then add as 'start->end', and if start == end then add as 'start(or end)'.
