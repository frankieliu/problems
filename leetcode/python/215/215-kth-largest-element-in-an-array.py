#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (45.32%)
# Total Accepted:    310.5K
# Total Submissions: 685.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        left = 0
        right = len(nums)-1
        while left <= right:

            print(nums, left, right)
            nk = partition(nums, left, right)
            print(nums, nk)

            if nk == k:
                return nums[k]
            elif nk < k:
                left = nk+1
            else:
                right = nk-1


def partition(n, left, right):
    """
       Uses the last element as the pivot

    """
    k = right  # pivot

    i = left
    j = right - 1
    # print(k, i, j)

    while i <= j:
        # print(n[i], n[k])
        if n[i] <= n[k]:
            i += 1
            continue
        else:
            # print(n)
            # print("swap{} {}".format(n[i], n[j]))
            n[i], n[j] = n[j], n[i]
            # print(n)
            j -= 1

    n[i], n[k] = n[k], n[i]
    return i

"""
a = [2,3,4,1,5,1,4]
j = partition(a, 0, 6)
print(a, j)
"""

test = True
if test:
    s = Solution()
    case = [True, True, True]
    if case[0]:
        Input = ([3,2,1,5,6,4], 2)
        print(s.findKthLargest(Input[0], Input[1]))
        # Output: 5

    if case[1]:
        Input = ([3,2,3,1,2,4,5,5,6], 4)
        print(s.findKthLargest(Input[0], Input[1]))
        # Output: 4

    if case[2]:
        Input = ([2,1], 2)
        print(s.findKthLargest(Input[0], Input[1]))
        # Output: 1
