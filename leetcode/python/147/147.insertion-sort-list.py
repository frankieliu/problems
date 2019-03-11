#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (36.13%)
# Total Accepted:    139.4K
# Total Submissions: 385.9K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
#
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
#
#
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        out = []
        while head:
            out.append(head)
            head = head.next
            # print(out[-1].val)

        out = sorted(out, key=lambda x: x.val)
        # print([x.val for x in out])

        for i in range(0, len(out)-1):
            out[i].next = out[i+1]
        out[len(out)-1].next = None
        return out[0]

test = False
if test:
    from ListNode.ListNode import ListNode
    ll = ListNode.make([5, 1, 2, 3, 4])
    s = Solution()
    print(s.insertionSortList(ll))
