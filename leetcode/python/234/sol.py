
11 lines, 12 with restore, O(n) time, O(1) space

https://leetcode.com/problems/palindrome-linked-list/discuss/64500

* Lang:    python3
* Author:  StefanPochmann
* Votes:   213

O(n) time, O(1) space. The second solution restores the list after changing it.

---

**Solution 1: *Reversed first half == Second half?***

Phase 1: Reverse the first half while finding the middle.  
Phase 2: Compare the reversed first half with the second half.

    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

---

**Solution 2: *Play Nice***

Same as the above, but while comparing the two halves, restore the list to its original state by reversing the first half back. Not that the OJ or anyone else cares.

    def isPalindrome(self, head):
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali
