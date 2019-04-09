
100% Runtime, 81% Memory, Java (BFS)

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/252162

* Lang:    java
* Author:  dannyli0818
* Votes:   0

```
class Solution {
    private Queue<TreeNode> queue = new LinkedList<>();
    private List<Integer> output = new ArrayList<>();
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        // let\'s find the TreeNodes starting from target with distance K.
        findChildrenInDepthDe(target, K);
        // now we will find the TreeNodes (maybe other side) with distance K from above to target
        searchAbove(root, target, K, 0);
        return output;
    }
    
    
    private int searchAbove(TreeNode node, TreeNode target, int k, int depth) {
        if(node == target) {
            return depth;
        }
        if(node == null) {
            return -1;
        }
        int left = searchAbove(node.left, target, k, depth + 1);
        if(left != -1) { // found target on left 
            if(left - depth == k) {// exactly on one side.
                output.add(node.val);
            }
            else {// will have to search on other side.
                // subtract 1 because we use node.right instead of the beginning root.
                findChildrenInDepthDe(node.right, k - left + depth - 1);
            }
            return left;
        }
        
        int right = searchAbove(node.right, target, k, depth + 1);
        if(right != -1) { // found target on right
            if(right - depth == k) {
                output.add(node.val);
            }
            else {
                findChildrenInDepthDe(node.left, k - right + depth - 1);
            }
            return right;
        }
        
        return -1;
    }
    
    // to find the valid children (Below the target node)
    private void findChildrenInDepthDe(TreeNode node, int de) {
        queue.offer(node);
        while(!queue.isEmpty()) {
            int size = queue.size();
            for(int i = 0; i < size; i++) {
                TreeNode ele = queue.poll();
                if(de == 0 && ele != null) {
                    output.add(ele.val);
                    continue;
                }
                if(ele != null) {
                    queue.offer(ele.left);
                    queue.offer(ele.right);
                }
            }
            de--;
        }
    }
    
}
