
DFS 3 ms 100.00% faster Java Accepted Solution

https://leetcode.com/problems/cousins-in-binary-tree/discuss/242476

* Lang:    java
* Author:  gaganleet619
* Votes:   0

```
public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        boolean foundOne = false;
        
        while(!queue.isEmpty()) {
        	int currentQueueSize = queue.size();
        	
        	while(currentQueueSize-- != 0) {
        		TreeNode temp = queue.poll();
        		// if this parent has both children, x and y 
        		if(temp.left != null && temp.right != null && (temp.left.val == x || temp.left.val == y) && 
        				(temp.right.val == x || temp.right.val == y)) {
        			return false;
        		}
        		
        		if(foundOne && ((temp.left != null && (temp.left.val == x || temp.left.val == y) || 
        				(temp.right != null && (temp.right.val == x || temp.right.val == y))))) {
        			return true;
        		}
        		
        		if(temp.left != null) {
        			if (temp.left.val == x || temp.left.val == y) {
	        			foundOne = true;
	    				continue;
        			}
        			queue.add(temp.left);
        		}
	        	if(temp.right != null) {
	    			if (temp.right.val == x || temp.right.val == y) {
	        			foundOne = true;
	    				continue;
	    			}
	    			queue.add(temp.right);
	    		}
        	}
        	
        	// if one child is found but other one is not found at same level/depth then we don\'t need to drill down further
        	if(foundOne) {
        		return false;
        	}
        }
        
        return false;
        
    }
```
