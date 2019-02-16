"""Given two integers n and k, return all possible combinations of k
numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Accepted
180,194
Submissions
396,894

"""

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.help(range(1, n+1), k)

    def help(self, a, k):

        if len(a) < k:
            return []
        if len(a) == k:
            return [list(a)]
        if k == 1:
            return [[x] for x in a]

        return ([
            [a[0]] + x
            for x in self.help(a[1::], k-1)] +
                self.help(a[1::], k))


s = Solution()
print(s.combine(4, 2))
