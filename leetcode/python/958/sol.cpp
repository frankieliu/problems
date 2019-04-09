
BFS easy to understand

https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/254419

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
    if(!root)
        return true;
    queue<TreeNode*> q;
    q.push(root);
    bool lack = false;
    while (!q.empty()) {
        int len = q.size();
        for(int i=0;i<len;i++){
            auto x = q.front();
            q.pop();
            if(x->left){
                if(lack)
                    return false;
                q.push(x->left);
            }
            else
                lack = true;
            if(x->right){
                if(lack)
                    return false;
                q.push(x->right);
            }
            else
                lack = true;
        }
    }
    return true;
    }
};
```
