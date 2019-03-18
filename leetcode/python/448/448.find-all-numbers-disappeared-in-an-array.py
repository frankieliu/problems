#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (52.46%)
# Total Accepted:    131.1K
# Total Submissions: 249.9K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#
#
class Solution:
    def findDisappearedNumbers(self, a):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Just mark the array where elements appear
        for i in range(len(a)):
            idx = abs(a[i]) - 1
            a[idx] = -abs(a[idx])
            # print(a)

        out = []
        for i in range(len(a)):
            if a[i] > 0:
                out.append(i+1)

        return out


test = True
if test:
    s = Solution()
    Input = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDisappearedNumbers(Input))
