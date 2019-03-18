
Simple python solution without extra space.

https://leetcode.com/problems/subsets-ii/discuss/30166

* Lang:    python3
* Author:  qqz003
* Votes:   106

    class Solution:
        # @param num, a list of integer
        # @return a list of lists of integer
        def subsetsWithDup(self, S):
            res = [[]]
            S.sort()
            for i in range(len(S)):
                if i == 0 or S[i] != S[i - 1]:
                    l = len(res)
                for j in range(len(res) - l, len(res)):
                    res.append(res[j] + [S[i]])
            return res

if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]
