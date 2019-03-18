
108ms python solution with heapq and avoid changing heap size

https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513

* Lang:    python3
* Author:  yyangbian
* Votes:   48

    def mergeKLists(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
    
        return dummy.next
