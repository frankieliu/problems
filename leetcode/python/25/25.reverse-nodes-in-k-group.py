#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (34.96%)
# Total Accepted:    163.7K
# Total Submissions: 468.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverseKGroup(self, head, k):

        def advance(prev, cur):
            """
            Makes cur point to prev
            And returns cur and cur.next
            """
            save_cur = cur
            save_next = cur.next
            cur.next = prev
            return (save_cur, save_next)

        def reverse_segment(ll, rr):
            """"
            Reverses a linked list beginning at from ll to rr (not inclusive)
            Returns the head and tail of the reversed segment
            """
            save_ll = ll
            prev = rr
            while True:
                prev, ll = advance(prev, ll)
                if ll == rr:
                    break
            return prev, save_ll

        def forward_k(cur, k):
            """
            Finds a node that is k away from cur,
            i.e. if k == 0, returns cur, if k == 1, return cur.next

            If cannot reach the kth node:
               returns (False, cur),
            else:
               returns (True, kth node)
            """
            save_cur = cur
            for _ in range(k):
                if cur is None:
                    return (False, save_cur)
                cur = cur.next
            return (True, cur)

        return_head = None
        prev_seg_tail = None

        rr = forward_k(head, k)
        while rr[0]:         # while there is something to reverse
            seg_head, seg_tail = reverse_segment(head, rr[1])
            if return_head is None:
                return_head = seg_head
            if prev_seg_tail:
                prev_seg_tail.next = seg_head
            head = rr[1]
            prev_seg_tail = seg_tail
            rr = forward_k(head, k)

        return return_head or head


test = True
if test:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

        def __repr__(self):
            if self.next is not None:
                return str(self.val) + "->" + self.next.__repr__()
            else:
                return str(self.val)

    def make(alist):
        nodelist = [ListNode(el) for el in alist]
        for i in range(len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        return nodelist[0]

    s = Solution()
    case = [False]*1 + [True] + [False]*1
    if case[0]:
        # Example:
        Input = make(range(1,6))
        print(s.reverseKGroup(Input, 3))
    if case[1]:
        # Example:
        Input = make(range(1,6))
        print(s.reverseKGroup(Input, 2))
