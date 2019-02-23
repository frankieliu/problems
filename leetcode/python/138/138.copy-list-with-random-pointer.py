#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.62%)
# Total Accepted:    215.1K
# Total Submissions: 839.7K
# Testcase Example:  '{}'
#
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        s = {}
        tmp = head
        while tmp:
            new = RandomListNode(tmp.label)
            s[tmp.label] = new
            tmp = tmp.next

        tmp = head
        while tmp:
            new = s[tmp.label]
            if tmp.next is not None:
                new.next = s[tmp.next.label]
            if tmp.random is not None:
                new.random = s[tmp.random.label]
            tmp = tmp.next

        return s[head.label]


test = False
if test:
    from ListNode.ListNode import ListNode
    RandomListNode = ListNode
    ll = ListNode.make([1, 2, 3, 4, 5])
    s = Solution()
    print(s.copyRandomList(ll))
