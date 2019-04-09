
Java Solution Level Traversal using Deque

https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106656

* Lang:    java
* Author:  addison
* Votes:   0

```
 public int widthOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        Deque<TreeNode> level = new LinkedList<>();
        
        level.add(root);
        int maxWidth = 0;

        while(!level.isEmpty()){
            // Remove leading null nodes
            while(level.peek() == null && !level.isEmpty()){ 
                level.remove();
            }
            // Remove ending null nodes
            while(level.peekLast() == null && !level.isEmpty()){ 
                level.removeLast();
            }
            
            int levelSize = level.size();
            maxWidth = Math.max(maxWidth, levelSize);
            
            for(int i = 0; i<levelSize;i++){
                TreeNode node = level.poll();

                if(node!=null){
                    level.add(node.left);
                    level.add(node.right);
                }else{
                    level.add(null);
                    level.add(null);
                }
            }
            
        }
        
        return maxWidth;
    }
```
