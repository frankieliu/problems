
Python solution - Simple Iterative

https://leetcode.com/problems/reverse-linked-list/discuss/58338

* Lang:    python3
* Author:  girikuncoro
* Votes:   12

I'm not sure if it's already posted here, but this is simple iterative approach. The idea is to change next with prev, prev with current, and current with next.

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
