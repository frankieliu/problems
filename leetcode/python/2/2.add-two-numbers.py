#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.34%)
# Total Accepted:    736.5K
# Total Submissions: 2.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val) + " " + str(self.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l11 = l1
        l22 = l2
        tmp = ListNode(None)
        l33 = tmp
        carry = 0
        while l11 or l22:
            sum = (l11 and l11.val or 0) + (l22 and l22.val or 0) + carry
            carry = sum // 10
            sum = sum % 10
            l33.next = ListNode(sum)
            l11 = l11 and l11.next or None
            l22 = l22 and l22.next or None
            l33 = l33.next
        if carry:
            l33.next = ListNode(carry)
        return tmp.next

test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        a = [2,3,4]
        b = [5,6,7]
        al = [ListNode(x) for x in a]
        bl = [ListNode(x) for x in b]
        for i in range(0,len(a)-1):
            al[i].next = al[i+1]
        for j in range(0,len(b)-1):
            bl[i].next = bl[i+1]
        print(s.addTwoNumbers(al[0], bl[0]))
    if case[1]:
        print(s.addTwoNumbers())
