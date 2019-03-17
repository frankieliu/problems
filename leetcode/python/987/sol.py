
based on python, easy to understand. Of course the runtime spend is a metaphysics

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/252699

* Lang:    python3
* Author:  thePrestige_yf
* Votes:   0


    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return [[]]
        dic = {}
        self.go(root, (0, 0), dic)
        result = []
        for i in sorted(dic.keys()):
            mid = sorted(dic[i])
            items = []
            for y, v in mid:
                items.append(v)
            result.append(items)
        return result
                
    def go(self, node, current, dic):
        x, y = current
        if node.left != None:
            self.go(node.left, (x-1, y+1), dic)
        if node.right != None:
            self.go(node.right, (x+1, y+1), dic)
        if x not in dic:
            dic[x] = [(y, node.val)]
        else:
            mid = dic[x]
            mid.append((y, node.val))
            dic[x] = mid
        return dic
