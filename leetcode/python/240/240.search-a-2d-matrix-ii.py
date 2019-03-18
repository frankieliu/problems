#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (40.07%)
# Total Accepted:    155.7K
# Total Submissions: 388.5K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
# Example:
#
# Consider the following matrix:
#
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# Given target = 5, return true.
#
# Given target = 20, return false.
#
#
class Solution:
    def searchMatrix(self, a, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # begin at bottom left
        n = len(a)
        m = len(a[0])

        i = n-1
        j = 0

        while True:
            print(a[i][j])

            # target is greater than element
            # then move up
            if a[i][j] < target:
                i -= 1
                if i < 0:
                    return False

            if a[i][j] > target:
                j += 1
                if j > m:
                    return False

            if a[i][j] == target:
                print(i, j)
                return True


test = True
if test:
    s = Solution()
    Example = [[1,4,7,11,15],
               [2,5,8,12,19],
               [3,6,9,16,22],
               [10,13,14,17,24],
               [18,21,23,26,30]]

    print(s.searchMatrix(Example, 5))
