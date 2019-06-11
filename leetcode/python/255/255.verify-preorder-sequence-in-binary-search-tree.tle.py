#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (43.00%)
# Total Accepted:    33.6K
# Total Submissions: 78.1K
# Testcase Example:  '[5,2,6,1,3]'
#
# Given an array of numbers, verify whether it is the correct preorder
# traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Consider the following binary search tree: 
#
#
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
#
# Example 1:
#
#
# Input: [5,2,6,1,3]
# Output: false
#
# Example 2:
#
#
# Input: [5,2,1,3,6]
# Output: true
#
# Follow up:
# Could you do it using only constant space complexity?
#
#
"""
312 valid
  3
 /
1
 \
  2

321 valid
    3
   /
  2
 /
1

123 valid
1
 \
  2
   \
    3
132 valid
213 valid

231 not valid!
"""

class Solution:
    def verifyPreorder(self, alist):

        # checks if valid preorder from i to j
        # checks if all the element in are bigger than k
        def helper(p, i, j, mx=None):
            # print("({},{}): {}".format(p[i], p[j], mx))
            # one element
            if (j-i) <= 0:
                return True

            # two elements
            if (j-i) == 1:
                if mx:
                    return p[i] > mx and p[j] > mx
                else:
                    return True

            # three elements:
            pivot = p[i]
            k = i
            while k <= j:
                if mx and p[k] < mx:
                    return False
                if p[k] > pivot:
                    break
                k += 1
            if k > j:
                # print("({},{}): {}, break @ {}".format(p[i], p[j], mx, k))
                return helper(p, i+1, k-1)
            # print("({},{}): {}, break: {}".format(p[i], p[j], mx, p[k]))
            return (helper(p, i+1, k-1) and
                    helper(p, k, j, p[i]))

        if len(alist) <= 1:
            return True
        return helper(alist, 0, len(alist)-1)


test = True
if test:
    s = Solution()
    case = [0, 0, 0, 1]
    if case[0]:
        print(s.verifyPreorder([5, 2, 1, 3, 6]))
    if case[1]:
        testcase = [1, 2, 3]
        print(s.verifyPreorder(testcase))
    if case[2]:
        testcase = [4, 2, 3, 1]
        print(s.verifyPreorder(testcase))
    if case[3]:
        testcase = [3, 2, 1, 5, 4, 6]
        print(s.verifyPreorder(testcase))
