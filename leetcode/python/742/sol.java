
Easiest and best Java Solution, treat tree as an Undirected graph

https://leetcode.com/problems/closest-leaf-in-a-binary-tree/discuss/109958

* Lang:    java
* Author:  SanD91
* Votes:   2

It is the closest leaf in terms of distance not value.
You can treat the tree as a undirected graph, get the node's adjacent nodes'. Create a map of it and start traversing from the 'k'. The first leaf to be encountered is the answer.
This is the fastest solution and running time would be O(n+m) same as BFS.
While creating the adjacent list for each node, you add an adjacent to both parent and child.
If 1 is parent of 2. Both 1, and 2 in the adjacent list will have each other. I hope it is clear.

```
class Solution {
    public int findClosestLeaf(TreeNode root, int k) {    
        if(root == null) {
            return 0;
        }
        
        Map<Integer, List<Integer>> adj = new HashMap<>();
        Deque<TreeNode> dq = new ArrayDeque<>();
        TreeNode node = null;
        List<Integer> cur = new ArrayList<>();
        List<Integer> next = new ArrayList<>();
        Map<Integer, TreeNode> tree = new HashMap<>();
        Deque<Integer> queue = new ArrayDeque<>();
        int max = 0;
        
        dq.offer(root);
        
        while(!dq.isEmpty()) {
            node = dq.poll();
            tree.put(node.val, node);
            max = Math.max(max, node.val);
            
            if(!adj.containsKey(node.val)) {
                cur = new ArrayList<>();
            } else {
                cur = adj.get(node.val);
            }
            
            if(node.left != null) {
                dq.offer(node.left);
                cur.add(node.left.val);
                
                if(!adj.containsKey(node.left.val)) {
                    next = new ArrayList<>();
                } else {
                    next = adj.get(node.left.val);
                }
                
                next.add(node.val);
                adj.put(node.left.val, next);
            }
            
            if(node.right != null) {
                dq.offer(node.right);
                cur.add(node.right.val);
                
                if(!adj.containsKey(node.right.val)) {
                    next = new ArrayList<>();
                } else {
                    next = adj.get(node.right.val);
                }
                
                next.add(node.val);
                adj.put(node.right.val, next);
            }
            
            adj.put(node.val, cur);
        }
        
        int[] visited = new int[max + 1];
        queue.offer(k);
        int val = 0;
        
        while(!queue.isEmpty()) {
            val = queue.poll();
            
            if(visited[val] != 1) {
                node = tree.get(val);
            
                if(node.left == null && node.right == null) {
                    return node.val;
                }
            
                cur = adj.get(val);
                if(cur != null && cur.size() > 0) {
                    for(int nextVal : cur) {
                        if(visited[nextVal] == 0) {
                            queue.offer(nextVal);
                            visited[nextVal] = -1;
                        }
                    }
                }
                
                visited[val] = 1;
            }
        }
        
        return 0;
    }
}
```
