"""82. Remove Duplicates from Sorted List II
Medium

661

65

Favorite

Share
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
Accepted
164,425
Submissions
515,213"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        h = head
        while h:
            # keep moving until you find a non-repeat
            n = h.next
            while n and n.val == h.val:
                n = n.next
            h.next = n
            h = n

        return head


s = Solution()
a = [1, 2, 3, 3, 4, 4, 5]
a = [1, 1, 1, 2, 3]
ll = []
for x in a:
    ll.append(ListNode(x))
for j in range(0, len(ll)-1):
    ll[j].next = ll[j+1]

h = s.deleteDuplicates(ll[0])

out = []
while h:
    out.append(str(h.val))
    h = h.next
print("->".join(out))
