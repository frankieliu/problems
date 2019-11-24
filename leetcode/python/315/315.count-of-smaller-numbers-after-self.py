#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.85%)
# Total Accepted:    67K
# Total Submissions: 181.8K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
#
class Solution:
    def countSmaller(self, nums):
        """

        Keys:
        1. merging from the right allows you to know how many elements
           have not been added yet
        2. merging recursively you add by each sub merge

        5 2 6 1

        5 2   6 1

        5 will see one on the right (2) +
        2 5

        6 will see one on the right (1) +
        1 6

        Note all the element in 16 are to the right of 25
        25 16

        so only 25 will get an update!
        2 +1
        5 +1
        """
        def merge_sort(n):
            mid = len(n)//2
            if mid:
                left, right = merge_sort(n[:mid]), merge_sort(n[mid:])
                for i in range(len(n))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        n[i] = left.pop()
                    else:
                        n[i] = right.pop()
            return n
        smaller = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return smaller


test = True
if test:
    sol = Solution()
    case = [False] * 0 + [True] + [False] * 1
    if case[0]:
        # Example:
        Input = [5, 2, 6, 1]
        # Output: [2,1,1,0]
        print(sol.countSmaller(Input))
