
Easy to understand level order traversal (Python) (beats 90%)

https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98797

* Lang:    python3
* Author:  pgl
* Votes:   0

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev_level = 0
        q = [(root, 1)]
        while len(q):
            node, level = q.pop(0)
            if level > prev_level:
                result = node.val
                prev_level = level
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return result
