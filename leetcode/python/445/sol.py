
python AC 138 ms. Reverse LL

https://leetcode.com/problems/add-two-numbers-ii/discuss/112021

* Lang:    python3
* Author:  vinhhoang
* Votes:   1

```
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)
        car = 0
        sen = ListNode(0)
        cur = sen
        while l1 or l2 or car:
            if l1 and l2:
                tot = l1.val + l2.val + car
                l1, l2 = l1.next, l2.next
            elif l1:
                tot = l1.val + car
                l1 = l1.next
            elif l2:
                tot = l2.val + car
                l2 = l2.next
            else:
                tot = car
            cur.next, car = ListNode(tot%10), tot//10
            cur = cur.next
            
        return self.reverseLL(sen.next)
            
        
    def reverseLL(self, head):
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
```
