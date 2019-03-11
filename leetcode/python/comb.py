# https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)
from functools import reduce

class Solution:
    def combinationSum3(self, k, n):
        combs = combination(k)
        return [c for c in combs if sum(c) == n]


# this is quite tricky to understand
# suppose you have [3,4,5] in your k-1 list
# then the k list would add the following
#
# 1,3,4,5
# 2,3,4,5
#
# Note that if you had [1,4,5] is your k-1 list
# then *nothing* would be added

def combination(k):
    combs = [[]]
    for _ in range(k):
        combs = [[first] + comb
                 for comb in combs
                 for first in range(1, comb[0] if comb else 10)
                 ]
        print(combs)
    return combs


def combination2(k):
    return reduce(
        lambda combs, _: [[first] + comb
                          for comb in combs
                          for first in range(1, comb[0] if comb else 10)],
        range(k), [[]])


# very clever solution
class Solution2:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        res = []
        cur = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.combinationSum3_helper(nums, k, n, 0, cur, res)
        return res

    # n is the number you are shooting for
    # cur is the current set of answers?
    # idx only iterate from idx to len(nums)-1

    def combinationSum3_helper(self, nums, k, n, idx, cur, res):

        # you have achieved the sum
        # return the current set of answers
        if n == 0:
            res.append(cur[:])

        for i in range(idx, len(nums)):
            # len(nums) - i
            if k > (len(nums)-i) or n < (i+1+i+k)*k/2 or n > (9 + 10 - k)*k/2:
                break

            # if the number of remaining elements not big enough
            # if the sum of the next k elements > n then no answer
            # if the sum of the last k elements < n then no answer either

            # this is path for having nums[i] as one of the elements
            cur.append(nums[i])

            # the subproblem then considers the remaining sum
            # - one less k
            # - one less number in nums
            # - move to next index
            # - current result

            self.combinationSum3_helper(nums, k-1, n-nums[i], i+1, cur, res)
            cur.pop()

print(combination2(2))
