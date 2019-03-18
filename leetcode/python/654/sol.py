
Concise Python Solution with Explanation

https://leetcode.com/problems/maximum-binary-tree/discuss/106224

* Lang:    python3
* Author:  csfaze2
* Votes:   1

Given a list, the maximum value will be the root of our tree. If the maximum value is at index `i`, the left value will be the maximum of `nums[:i]` and the right value will be the maximum of `nums[i + 1:]`. This rule can be recursively applied for any subtree, so all you have to do is call the method for the left and right subtrees, and the node references will fall in place accordingly. 

```
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        i = nums.index(max(nums))

        node = TreeNode(nums[i])

        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])

        return node
```
