
Concise C++ and Python Solutions

https://leetcode.com/problems/trim-a-binary-search-tree/discuss/107034

* Lang:    python3
* Author:  yang_fan
* Votes:   0

The idea is inspired by [shawngao](https://discuss.leetcode.com/topic/102034/java-solution-6-liner)

C++ solution:
```
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if(!root) return root;
        if(root->val<L)return trimBST(root->right,L,R);
        if(root->val>R)return trimBST(root->left,L,R);
        root->left=trimBST(root->left,L,R);
        root->right=trimBST(root->right,L,R);
        return root;
      }
};
```
Python solution:
```
class Solution(object):
    def trimBST(self, root, L, R):
        if not root:return None
        if root.val<L: return self.trimBST(root.right,L,R)
        if root.val>R: return self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        root.left=self.trimBST(root.left,L,R)
        return root
```
