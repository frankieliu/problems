"""22. Generate Parentheses
Medium

2141

136

Favorite

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Accepted
280.7K
Submissions
539.5K
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.help(2*n, 0)

    def help(self, n, diff):
        print(n, diff)

        if (n % 2) != (diff % 2):
            return []

        if n == 0:
            if diff == 0:
                return [""]
            else:
                return []

        a = ["(" + x for x in self.help(n-1, diff+1)]
        if diff > 0:
            b = [")" + x for x in self.help(n-1, diff-1)]
        else:
            b = []

        return a + b


s = Solution()
#print(s.generateParenthesis(2))
print(s.help(4, 0))
