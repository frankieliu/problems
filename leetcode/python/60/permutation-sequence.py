"""60. Permutation Sequence
Medium

658

181

Favorite

Share
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Accepted
124,983
Submissions
393,090"""

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.helper(range(1, n+1), k)

    def fac(self, n):
        out = 1
        for i in range(n,0,-1):
            out *= i
        return out

    def helper(self, ll, k):
        # print("Solving:", ll, k)
        if k == 1:
            return "".join([str(x) for x in ll])

        n = len(ll)
        sub = self.fac(n-1)

        # This tells you which bin it belongs to
        bin = (k-1) // sub
        inbin = (k-1) % sub + 1
        # print(bin, ll[bin], inbin)
        return (str(ll[bin]) +
                self.helper([x for x in ll if x != ll[bin]],
                            inbin))

s = Solution()
print(s.getPermutation(4,15))
