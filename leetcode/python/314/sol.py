
Python solution

https://leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/76424

* Lang:    python3
* Author:  StefanPochmann
* Votes:   82

    def verticalOrder(self, root):
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
