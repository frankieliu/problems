
Simple & clear python solution

https://leetcode.com/problems/remove-linked-list-elements/discuss/57461

* Lang:    python3
* Author:  hoffa
* Votes:   9

First we remove all (if any) target nodes from the beginning (we do it because the removing logic is slightly different from when the node is not in the head). After that we just loop over all nodes, if the next one is one that should be removed, just get it out of the list by moving the next pointer to the next-next node. Otherwise just move along the list.

    class Solution(object):
        def removeElements(self, head, val):
            while head is not None and head.val == val:
                head = head.next
            current = head
            while current is not None:
                if current.next is not None and current.next.val == val:
                    current.next = current.next.next
                else:
                    current = current.next
            return head
