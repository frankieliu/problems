
Simple Python 91% fast, still need advice

https://leetcode.com/problems/find-duplicate-file-in-system/discuss/259188

* Lang:    python3
* Author:  dixitomkar1809
* Votes:   0

How do i improve my space complexity here, its better than about 77% of submissions ??
```
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        solution = []
        hmap = collections.defaultdict(list)
        for path in paths:
            splitText = path.strip().split()
            path = splitText[0]
            files = splitText[1:]
            for file in files:
                fileName, content = file.split("(")
                content = content[:-1]
                hmap[content].append(path+"/"+fileName)
        for content in hmap:
            if len(hmap[content]) > 1:
                solution.append(hmap[content])
            
        return solution
```
