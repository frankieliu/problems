#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (36.03%)
# Total Accepted:    6.7K
# Total Submissions: 18.5K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        
