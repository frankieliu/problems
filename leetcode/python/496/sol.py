
Python solution using stack and hash table.

https://leetcode.com/problems/next-greater-element-i/discuss/114093

* Lang:    python3
* Author:  lzyacht
* Votes:   0

Python solution using stack and hash table.

```
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        for num in nums2:
            while stack != [] and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            if num in dic.keys():
                res.append(dic[num])
            else:
                res.append(-1)

        return res
```
