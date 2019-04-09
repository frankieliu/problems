
Simple Java Recursive Solution

https://leetcode.com/problems/diameter-of-binary-tree/discuss/101214

* Lang:    java
* Author:  fabrizio3
* Votes:   0

```
private int maxDiameter = 0;
public int diameterOfBinaryTree(TreeNode root) {
    if(root==null) return 0;
    maxDepth(root);
    return this.maxDiameter;
}
public int maxDepth(TreeNode root) {
    int leftDepth = root.left==null ? 0 : maxDepth(root.left)+1;
    int rightDepth = root.right==null ? 0 : maxDepth(root.right)+1;
    this.maxDiameter = Math.max(this.maxDiameter, leftDepth+rightDepth);
    return Math.max(leftDepth,rightDepth);
}
```
