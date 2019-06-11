#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
# https://leetcode.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (33.18%)
# Total Accepted:    6.4K
# Total Submissions: 19.2K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# Two strings X and Y are similar if we can swap two letters (in different
# positions) of X, so that it equals Y.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars",
# "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
# even though they are not similar.  Formally, each group is such that a word
# is in the group if and only if it is similar to at least one other word in
# the group.
#
# We are given a list A of strings.  Every string in A is an anagram of every
# other string in A.  How many groups are there?
#
# Example 1:
#
#
# Input: ["tars","rats","arts","star"]
# Output: 2
#
# Note:
#
#
# A.length <= 2000
# A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.
# The judging time limit has been increased for this question.
#
#
#


class union:
    def __init__(self, num):
        self.p = [None] * num
        for i in range(0, num):
            self.p[i] = i

    def parent(self, i):
        if self.p[i] == i:
            return i
        else:
            return self.parent(self.p[i])

    def join(self, a, b):
        a_par = self.parent(a)
        b_par = self.parent(b)
        self.p[a] = b_par


class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def similar(a, b):
            diff = 0
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        uf = union(len(A))

        for i in range(0, len(A)):
            for j in range(i, len(A)):
                if similar(A[i], A[j]):
                    uf.join(j, i)


test = True
if test:
    s = Solution()
    Input = ["tars", "rats", "arts", "star"]
    print(s.numSimilarGroups(Input))
