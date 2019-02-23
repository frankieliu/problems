#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (29.46%)
# Total Accepted:    139.5K
# Total Submissions: 473.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        t = head
        a = []
        while t:
            a.append(t)
            t = t.next
        if len(a) < 3:
            return
        # print(a[1].next.val)
        for i in range(0, len(a)//2):
            tmp = a[i].next
            a[i].next = a[~i]
            if tmp == a[~i]:
                a[~i].next = None
            else:
                a[~i].next = tmp
        tmp.next = None


test = False
if test:
    from ListNode.ListNode import ListNode
    ll = ListNode.make([1, 2, 3, 4, 5])
    s = Solution()
    print(s.reorderList(ll))
    print(ll)
