
inorder and stack

https://leetcode.com/problems/increasing-order-search-tree/discuss/254400

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
void inorder(TreeNode* root,stack<TreeNode*>& s){
    if(root){
        inorder(root->left, s);
        s.push(root);
        inorder(root->right, s);
    }
}

TreeNode* increasingBST(TreeNode* root){
    stack<TreeNode*> s;
    inorder(root, s);
    TreeNode* head = nullptr;
    if(!s.empty()){
        head = s.top();
        s.pop();
    }
    head -> left = nullptr;
    head -> right = nullptr;
    while (!s.empty()) {
        s.top()->left = nullptr;
        s.top()->right = head;
        head = s.top();
        s.pop();
    }
    return head;
}
};
```
