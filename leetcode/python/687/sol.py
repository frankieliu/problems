
[Python/Java] simple dfs solution

https://leetcode.com/problems/longest-univalue-path/discuss/246059

* Lang:    python3
* Author:  Max_I
* Votes:   1

Python:
```
    def longestUnivaluePath(self, root):
        """
        """
        def dfs(node, prev_val):
            if node is None:
                return 0
            left=dfs(node.left, node.val)
            right=dfs(node.right, node.val)
            self.max_val=max(self.max_val, left+right)
            if node.val==prev_val:
                return max(left, right)+1
            return 0
        self.max_val=0
        if root is None:
            return 0
        dfs(root,root.val)
        return self.max_val
```

Java:
```
    private  int maxVal=0;
    public int longestUnivaluePath(TreeNode root) {
        if(root ==null)
            return 0;
        this.dfs(root,root.val);
        return  this.maxVal;
    }
    private int dfs(TreeNode node, int prevVal){
        if (node ==null){
            return  0;
        }
        int left=this.dfs(node.left,node.val);
        int right=this.dfs(node.right,node.val);
        this.maxVal=Math.max(this.maxVal, left+right);
        if (node.val==prevVal){
            return Math.max(left,right)+1;
        }
        return  0;
    }
```
