
short Java solution beats 98%

https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/237271

* Lang:    java
* Author:  dreamill
* Votes:   1

```
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> list = new ArrayList<>();
        if(root == null) return list;
        List<Integer> list2 = new ArrayList<>();
        list2.add(root.val);
        list.add(list2);
        getChildren(list, root, 0);
        return list;
    }
    public void getChildren(List<List<Integer>> list, Node node, int level){
        if(node == null || node.children.isEmpty()) return;
        List<Integer> chList;
        if(list.size() == level+1) chList = new ArrayList<>(); 
        else chList = list.get(level+1); //if already have, no need to new it
        for(Node node1 : node.children)chList.add(node1.val);
        if(list.size() == level+1) list.add(chList); //without the if, it will add chList repeatedly
        for(Node node2 : node.children) getChildren(list, node2, level+1); 
    }
}
```
