
3 short Python solutions

https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802

* Lang:    python3
* Author:  StefanPochmann
* Votes:   111

**Value-Shifting - AC in 64 ms**

My first solution is "cheating" a little. Instead of really removing the nth *node*, I remove the nth *value*. I recursively determine the indexes (counting from back), then shift the values for all indexes larger than n, and then always drop the head.

    class Solution:
        def removeNthFromEnd(self, head, n):
            def index(node):
                if not node:
                    return 0
                i = index(node.next) + 1
                if i > n:
                    node.next.val = node.val
                return i
            index(head)
            return head.next

---

**Index and Remove - AC in 56 ms**

In this solution I recursively determine the indexes again, but this time my helper function removes the nth node. It returns two values. The index, as in my first solution, and the possibly changed head of the remaining list.

    class Solution:
        def removeNthFromEnd(self, head, n):
            def remove(head):
                if not head:
                    return 0, head
                i, head.next = remove(head.next)
                return i+1, (head, head.next)[i+1 == n]
            return remove(head)[1]

---

**n ahead - AC in 48 ms**

The standard solution, but without a dummy extra node. Instead, I simply handle the special case of removing the head right after the fast cursor got its head start.

    class Solution:
        def removeNthFromEnd(self, head, n):
            fast = slow = head
            for _ in range(n):
                fast = fast.next
            if not fast:
                return head.next
            while fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head
