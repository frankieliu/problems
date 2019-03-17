
Python3 Linked List

https://leetcode.com/problems/design-linked-list/discuss/240682

* Lang:    python3
* Author:  eamanbekov
* Votes:   1

I used LeetCode\'s own `ListNode` implementation, if you wonder where did I get `ListNode` :)
Hope this helps you.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def increaseLength(self):
        self.len += 1
    
    def decreaseLength(self):
        self.len -= 1
    
    def getNode(self, index: int) -> ListNode:
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    
    def get(self, index: \'int\') -> \'int\':
        if index < 0 or index >= self.len:
            return -1
        
        return self.getNode(index).val

    def addAtHead(self, val: \'int\') -> \'None\':
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.increaseLength()

    def addAtTail(self, val: \'int\') -> \'None\':
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = ListNode(val)
        
        if self.len == 0:
            self.head = new_tail
        else:
            tail = self.getNode(self.len-1)
            tail.next = new_tail

        self.increaseLength()

    def addAtIndex(self, index: \'int\', val: \'int\') -> \'None\':
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len:
            return

        if index == self.len:
            self.addAtTail(val)
        else:
            node_before = self.getNode(index-1)
            node_after = self.getNode(index)

            new_node = ListNode(val)

            node_before.next = new_node
            new_node.next = node_after

            self.increaseLength()

    def deleteAtIndex(self, index: \'int\') -> \'None\':
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.len:
            return
        
        node_to_delete = self.getNode(index)
        del node_to_delete
        if index == 0:
            new_head = self.get(1)
            self.head = new_head
        else:
            node_before = self.getNode(index-1)
            node_after = self.getNode(index+1)
            node_before.next = node_after
        self.decreaseLength()
```
