class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def push_left(root, s):
    while root:
        s.append(root)
        root = root.left


def inorder_stack(root):
    s = []
    push_left(root, s)
    while s:
        t = s.pop()
        print(t.val)
        push_left(t.right, s)


# Morris
"""
1. Initialize current as root

2. While current is not NULL

   If current does not have left child

      a) Print current’s data
      b) Go to the right, i.e., current = current->right

   Else:

      Make predecessor's right child = current (back link)

      a. if predecessor's right child already points to current
         print current.data
         restore right child to null
         current = current -> right (descend right)

         # i.e. you print the parent after left is done
         # i.e. print order is left - root - right

      b. if predecessor's right child is null
         1. set the back link: make pred.right = current
            (pred = right child of rightmost node in current.left)
         2. current = current -> left (descend left)

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

inorder_stack(t[0])
