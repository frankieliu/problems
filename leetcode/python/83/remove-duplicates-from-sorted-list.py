"""83. Remove Duplicates from Sorted List
Easy

611

65

Favorite

Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
Accepted
286,897
Submissions
691,051"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        origin = head
        while head is not None:
            while head.next is not None and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return origin
