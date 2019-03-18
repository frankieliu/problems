
Clean python code

https://leetcode.com/problems/sort-list/discuss/46710

* Lang:    python3
* Author:  lime66
* Votes:   66

    class Solution(object):
        def merge(self, h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next
        
            tail.next = h1 or h2
            return dummy.next
        
        def sortList(self, head):
            if not head or not head.next:
                return head
        
            pre, slow, fast = None, head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None

            return self.merge(*map(self.sortList, (head, slow)))
