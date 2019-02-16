#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (31.95%)
# Total Accepted:    165K
# Total Submissions: 516.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:

    def find_next(self, h):
        if h is None:
            return h
        if h.next is None:
            return h
        if h.next.val != h.val:
            return h
        c = h.next
        while c is not None and c.val == h.val:
            c = c.next
        return self.find_next(c)

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = self.find_next(head)
        h0 = h  # save it
        while h is not None:
            h.next = self.find_next(h.next)
            h = h.next
        return h0

test = False
if test:
    from ListNode.ListNode import ListNode
    ll = ListNode.make([1,2,3,3,4,4,5])
    s = Solution()
    print(s.deleteDuplicates(ll))
