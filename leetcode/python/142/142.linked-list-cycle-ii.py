#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.54%)
# Total Accepted:    190.6K
# Total Submissions: 624.2K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
# Follow up:
# Can you solve it without using extra space?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        h = head
        f = head
        while h.next and f.next and f.next.next:
            # print(h.val, f.val)
            h = h.next
            f = f.next.next   # move two steps
            if h == f:
                break

        if h.next is None or f.next is None or f.next.next is None:
            return None

        h = head
        while h and f:
            if h == f:
                break
            h = h.next
            f = f.next
        return h


test = False
if test:
    from ListNode.ListNode import ListNode
    ll = ListNode.make([1,2,3,4,5])
    tmp = ll
    a = []
    while tmp is not None:
        a.append(tmp)
        tmp = tmp.next
    print(len(a), a[-1].val)
    a[-1].next = a[0]

    s = Solution()
    b = s.detectCycle(ll)
    print(b.val)
