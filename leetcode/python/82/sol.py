
Python in-place solution with dummy head node.

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336

* Lang:    python3
* Author:  caikehe
* Votes:   48

        
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
