"""24. Swap Nodes in Pairs
Medium

825

75

Favorite

Share
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Accepted
264.3K
Submissions
626.3K
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        new_head = self.swapOnce(head)

        A = new_head
        while A is not None and A.next is not None:
            B = A.next
            C = B.next
            B.next = self.swapOnce(C)
            A = B.next

        return new_head

    def swapOnce(self, ptr):

        if ptr is None or ptr.next is None:
            return ptr

        A = ptr
        B = ptr.next
        C = ptr.next.next

        A.next = C
        B.next = A
        return B

def stringToIntegerList(input):
    import json
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    # lines = readlines()
    lines = iter(["[1,2,3,4]"])

    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
