"""86. Partition List
Medium

532

143

Favorite

Share

Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each
of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Accepted
149,024
Submissions
414,844
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h = head
        less = None
        more = None
        mhead = None
        lhead = None

        while h:
            if h.val < x:
                # print("less +", h.val)
                if less is None:
                    lhead = h
                else:
                    less.next = h
                less = h
            else:
                # print("more +", h.val)
                if more is None:
                    mhead = h
                else:
                    more.next = h
                more = h
            h = h.next

        if less:
            less.next = mhead
            if more:
                more.next = None
            return lhead

        if more:
            return mhead

        return None


def ListNodeToString(head):
    out = []
    while head:
        out.append(str(head.val))
        head = head.next
    return "->".join(out)


def makeListNode(hs):
    h = [int(x) for x in hs.split("->")]
    ll = []
    for el in h:
        ll.append(ListNode(el))
    for i in range(0, len(ll)-1):
        ll[i].next = ll[i+1]
    return ll[0]


s = Solution()
hs = "1->4->3->2->5->2"
hs = "1"
h0 = makeListNode(hs)
print(ListNodeToString(h0))
h1 = s.partition(h0, 3)
print(ListNodeToString(h1))
