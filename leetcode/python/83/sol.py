
Simple iterative Python 6 lines, 60 ms

https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28621

* Lang:    python3
* Author:  zhuyinghua1203
* Votes:   30

    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
