
Java - via subtree serialization for all nodes - easy to understand

https://leetcode.com/problems/find-duplicate-subtrees/discuss/106052

* Lang:    java
* Author:  prakhar241
* Votes:   0

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    List<String> list = new ArrayList<>();
    List<TreeNode> nodes = new ArrayList<>();
    List<String> done = new ArrayList<>();
    
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        
        
        if (root == null) return nodes;
        
        if (root != null) {
            StringBuilder sb = new StringBuilder();
            Serialize(root, sb);
            String s = sb.toString();
            
            if (!list.contains(s)) {                   
                list.add(s);                
            } else {       
                if (!done.contains(s)) {  
                    nodes.add(root);
                    done.add(s);  
                }                    
            }
            
            findDuplicateSubtrees(root.left);
            findDuplicateSubtrees(root.right);
        }
        
        return nodes;
        
    }
    
    void Serialize(TreeNode root, StringBuilder sb) {       
        String del = ",";
        sb.append(((root == null)? "null": root.val) + del);
        if (root != null) {
            Serialize(root.left, sb);
            Serialize(root.right, sb);
        }        
    }    
}
