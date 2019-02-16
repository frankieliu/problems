"""61. Rotate List
Medium

483

755

Favorite

Share

Given a linked list, rotate the list to the right by k places, where k
is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
Accepted
171,815
Submissions
655,796

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def length(self, head):
        i = 0
        p = head
        while p is not None:
            p = p.next
            i += 1
        return i

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k < 1:
            return head

        if head is None:
            return head

        s = self.length(head)
        k = k % s

        # two pointers
        p0 = head
        prev0 = None

        p1 = head
        prev1 = None

        for i in range(0, k):
            prev0 = p0
            p0 = p0.next
            if p0 is None:
                p0 = head
            # print(prev0.val, "->", p0.val)

        # print("Stage 2")
        while p0 != None:
            prev0 = p0
            p0 = p0.next
            prev1 = p1
            p1 = p1.next
            if p1 is None:
                p1 = head
            if p0 is not None:
                # print(prev0.val, "->", p0.val)
                pass
            else:
                # print(prev0.val, "-> None")
                pass
            if p1 is not None:
                # print(prev1.val, "->", p1.val)
                pass
            else:
                # print(prev1.val, "-> None")
                pass

        # print([x.val if x is not None else
        #       None for x in [prev0, p0, prev1, p1]])

        # print("Clean up")

        # point the end to the beginning
        prev0.next = head
        # print(prev0.val, "->", prev0.next.val)

        # terminate at the middle
        prev1.next = None
        # print(prev1.val, "-> None")

        # return the new head
        if p1 is None:
            p1 = head
        # print("head -> ", p1.val)

        return p1


from collections import defaultdict

def print_linked_list(h):
    out = []
    while h is not None:
        out.append(h.val)
        h = h.next
    print(out)

def create_linked_list(n):
    ll = [ListNode(i) for i in range(1, n+1)]
    for i in range(0, len(ll)):
        if i == len(ll)-1:
            ll[i].next = None
        else:
            ll[i].next = ll[i+1]
    return ll[0]


s = Solution()

# Create this one
# Input: 1->2->3->4->5->NULL, k = 2
i1 = create_linked_list(3)
h = s.rotateRight(i1, 20)
print_linked_list(h)
