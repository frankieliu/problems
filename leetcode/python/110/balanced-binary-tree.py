"""110. Balanced Binary Tree
Easy

918

80

Favorite

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Accepted
279,404
Submissions
699,641
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "({} {} {})".format(self.val, self.left, self.right)


class Solution:

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bd = self.isBalDepth(root)
        return bd[0]

    def isBalDepth(self, root):
        if root is None:
            return (True, 0)

        ll = self.isBalDepth(root.left)
        rr = self.isBalDepth(root.right)
        # print(root, ll, rr)
        return (
            abs(ll[1] - rr[1]) <= 1 and
            ll[0] and
            rr[0], max(ll[1], rr[1]) + 1)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    #lines = readlines()

    lines = iter(["[1,2,2,3,3,null,null,4,4]"])
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().isBalanced(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
