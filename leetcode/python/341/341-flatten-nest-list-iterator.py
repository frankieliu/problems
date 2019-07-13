#
# @lc app=leetcode id=341 lang=python
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (46.38%)
# Total Accepted:    95.4K
# Total Submissions: 205.6K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
#
# Example 1:
#
#
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,1,2,1,1].
#
#
# Example 2:
#
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,4,6].
#
#
#
#
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.i = 0
        self.nl = None
        self.l = nestedList

    def next(self):
        """
        :rtype: int
        """
        i = self.i
        print("next", i)
        if self.l[i].isInteger():
            self.i += 1
            print("next int: ", self.l[i].getInteger())
            return self.l[i].getInteger()
        else:
            if self.nl is None:
                self.nl = NestedIterator(self.l[i].getList())
            print("Calling next's hasNext")
            if self.nl.hasNext():
                out = self.nl.next()
                print("next inside: ", out)
                return out
            else:
                print("finished nl")
                self.i += 1
                self.nl = None
                return self.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        i = self.i
        print("hasNext", i, self.nl)
        if i >= len(self.l):
            print("hasNext > len(l)")
            return False
        if self.l[i].isInteger():
            print("hasNext is int")
            return True
        else:
            print("hasNext is list")
            if len(self.l[i].getList()) == 0:
                self.i += 1
                return self.hasNext()
            else:
                print("hasNext is non zero list")
                if self.nl is None:
                    return True
                else:
                    return self.nl.next()
        return True



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
