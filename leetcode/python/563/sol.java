
Java no global val, no multiple repeated traversal

https://leetcode.com/problems/binary-tree-tilt/discuss/242311

* Lang:    java
* Author:  monsoonwinds7
* Votes:   0

```
class Solution {
    public int findTilt(TreeNode root) {
     
        ArrayList<Integer> tilt = new ArrayList();
        
        sumNodes(root, tilt);
        
        int sum =0;
        for (Integer t: tilt) {
            sum = sum + t;
        }
        return sum;
    }
    
    private int sumNodes(TreeNode root , List<Integer> tilt) {
        if (root == null) {
            return 0;
        }
        
        int left = sumNodes(root.left , tilt);
        int right = sumNodes(root.right , tilt);
        
        tilt.add(Math.abs(left -right));
        return left + right + root.val;
        
    }
    
}
```
