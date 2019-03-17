
AC Python 192ms solution

https://leetcode.com/problems/insertion-sort-list/discuss/46432

* Lang:    python3
* Author:  dietpepsi
* Votes:   19

    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next


    # 21 / 21 test cases passed.
    # Status: Accepted
    # Runtime: 192 ms
    # 97.05%

Of course, the solution is still O(n^2) in the worst case, but it can be faster than most implements under given test cases.

Two key points are: (1) a quick check see if the new value is already the largest (2) only refresh the search pointer p when the target is before it, in other words smaller.
