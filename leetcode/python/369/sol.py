
Short reverse+increase+reverse

https://leetcode.com/problems/plus-one-linked-list/discuss/84139

* Lang:    python3
* Author:  StefanPochmann
* Votes:   15

Inspired by others I had to try it myself...

---

Solution 1, reverse and then increase while reversing back
-

    def plusOne(self, head):
        tail = None
        while head:
            head.next, head, tail = tail, head.next, head
        carry = 1
        while tail:
            carry, tail.val = divmod(carry + tail.val, 10)
            if carry and not tail.next:
                tail.next = ListNode(0)
            tail.next, tail, head = head, tail.next, tail
        return head

---

Solution 2, with pure reverse helper
-

    def plusOne(self, head):
        def reverse(head):
            rev = None
            while head:
                head.next, head, rev = rev, head.next, head
            return rev
        head = node = reverse(head)
        while node.val == 9:
            node.val = 0
            node.next = node = node.next or ListNode(0)
        node.val += 1
        return reverse(head)

---

If you don't like that bottom while-loop, here's a more normal way I guess:

        while node.val == 9:
            node.val = 0
            if not node.next:
                node.next = ListNode(0)
            node = node.next
