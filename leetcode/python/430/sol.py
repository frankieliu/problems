
Python Iterative Solution using stack

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/232643

* Lang:    python3
* Author:  pranavdave893
* Votes:   0

```
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stck = []
        exit = False
        pointer = head
        while not exit:
            while (pointer and pointer.next) or (pointer and pointer.child):
                if pointer.child:
                    
                    stck.append(pointer.next)
                    pointer.next = pointer.child
                    pointer.child.prev = pointer
                    pointer.child = None
                    pointer = pointer.next
                else:
                    pointer = pointer.next
                
            if stck:
                flat = stck.pop()
                if pointer:
                    pointer.next = flat
                if flat:
                    flat.prev = pointer
            else:
                exit = True
                break
            pointer = flat
            continue
        return head
```
