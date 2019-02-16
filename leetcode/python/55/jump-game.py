"""55. Jump Game
Medium

1456

164

Favorite

Share

Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false

Explanation: You will always arrive at index 3 no matter what. Its
             maximum jump length is 0, which makes it impossible to
             reach the last index.

Accepted
222,032
Submissions
719,760

"""


class Solution:
    def canJump(self, n):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        begin at the last index mark all the index that can reach it
        """
        if len(n) == 0:
            return False
        if len(n) == 1:
            return True

        b = [False] * len(n)
        i = len(n) - 1
        b[i] = True
        i -= 1
        while i >= 0:
            for j in range(i+1, min(i+n[i]+1, len(n))):
                if b[j]:
                    b[i] = True
                    break
            i -= 1
        return b[0]


s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([]))
print(s.canJump([2]))
