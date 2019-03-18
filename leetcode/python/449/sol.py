
Python solution serializing as Preorder list

https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93195

* Lang:    python3
* Author:  redtree1112
* Votes:   0

The remarkable difference from serialize/deserialize Binary Tree ( https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ ) is, **BST can be constructed just from its preorder array** while a general binary tree requires both [in-order and and pre-order](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/#/description ) or [in-order and post-order](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/#/description).

So for serializing BST, just perform a pre-order traversal and stringify the result array.
Deserialization can be also done in the same manner as:
http://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/

```
class Codec:
    def serialize(self, root):
        if not root:
            return "none"
        cur = root
        
        res = ""
        stack = []
        while cur:
            res += str(cur.val) + ","
            
            if cur.right:
                stack.append(cur)
            
            if cur.left:
                cur = cur.left
            elif not stack:
                break
            else:
                cur = stack.pop()
                cur = cur.right
        return res[:-1] # remove the last ","
          
    def deserialize(self, data):
        if data == "none":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        cur = root
        
        stack = []
        for i in range(1, len(vals)):
            val = int(vals[i])
            
            if val < cur.val:
                cur.left = TreeNode(val)
                stack.append(cur)
                cur = cur.left
            else:
                while stack and cur.val < val:
                    if stack[-1].val < val:
                        cur = stack.pop()
                    else:
                        break
                cur.right = TreeNode(val)
                cur = cur.right
        return root
            
```
