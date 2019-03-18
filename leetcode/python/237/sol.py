
Python two lines solution, copy value and then delete the next node.

https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/65456

* Lang:    python3
* Author:  caikehe
* Votes:   17

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
