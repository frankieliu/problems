"""11. Container With Most Water
Medium

2439

393

Favorite

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.





The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Accepted
290,285
Submissions
704,388"""

class Solution:
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        slen = len(h)
        if slen <= 1:
            return 0

        p1 = 0
        p2 = slen - 1

        mx = 0
        while p2 > p1:
            lt = h[p1]
            rt = h[p2]
            area = (p2 - p1) * min(lt, rt)
            if area > mx:
                mx = area
            if lt < rt:
                p1 += 1
            else:
                p2 -= 1

        return mx

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
