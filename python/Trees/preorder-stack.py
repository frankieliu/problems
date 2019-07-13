class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_stack(root):
    s = []
    s.append(root)
    while s:
        t = s.pop()
        print(t.val)
        if t.right:
            s.append(t.right)
        if t.left:
            s.append(t.left)


# Morris
"""
Morris traversal for Preorder

Using Morris Traversal, we can traverse the tree without using stack
and recursion. The algorithm for Preorder is almost similar to Morris
traversal for Inorder.

1. If left child is null, print the current node data. Move to right
   child.

   Else, Make the right child of the inorder predecessor point to the
   current node. Two cases arise:

   a. The right child of the inorder predecessor already points to the
      current node. Set right child to NULL. Move to right child of
      current node.

   b. The right child is NULL. Set it to current node. Print current
      node’s data and move to left child of current node.

      # i.e. you print the root before descending left
      # i.e. print order is root - left - right

2. Iterate until current node is not NULL.
"""

t = []
for i in range(1, 8):
    t.append(TreeNode(i))

for i in range(len(t)):
    left = 2*i+1
    right = 2*i+2
    if left < len(t) and t[left]:
        t[i].left = t[left]
    if right < len(t) and t[right]:
        t[i].right = t[right]

preorder_stack(t[0])
