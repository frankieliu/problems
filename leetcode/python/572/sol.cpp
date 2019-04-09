
4 lines C++ DFS

https://leetcode.com/problems/subtree-of-another-tree/discuss/102748

* Lang:    cpp
* Author:  zefengsong
* Votes:   0

```
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s) return !t;
        return isEqual(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }
    
    bool isEqual(TreeNode* p, TreeNode* t){
        if(!p || !t) return !p && !t;
        return p->val == t->val && isEqual(p->left, t->left) && isEqual(p->right, t->right);
    }
};
```
