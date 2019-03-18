
Simple python solution

https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98135

* Lang:    python3
* Author:  yang_fan
* Votes:   0

Just solve the problem in regular way, and may not meet the follow-up requirement.
```
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        stack=[root]
        dic={}
        while stack:
            node=stack.pop()
            dic[node.val]=dic.get(node.val,0)+1
            if not node.left and not node.right:continue
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        max_val=max(dic.values())
        result=[]
        for key in dic.keys():
            if dic[key]==max_val:
                result.append(key)
        return result
```
