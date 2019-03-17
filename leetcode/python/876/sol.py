
Python one pass

https://leetcode.com/problems/middle-of-the-linked-list/discuss/251643

* Lang:    python3
* Author:  Huayra
* Votes:   2

Fast pointer runs twice as fast than slow pointer, which will land slow to the middle when fast reaches the end.
O(n) Time / O(1) Space
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
