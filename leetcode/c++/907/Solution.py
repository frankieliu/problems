class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
