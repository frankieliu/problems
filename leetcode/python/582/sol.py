
python bfs, dfs, stack,queue, hashmap, AC

https://leetcode.com/problems/kill-process/discuss/112346

* Lang:    python3
* Author:  vinhhoang
* Votes:   3

queue: 863 ms
```
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        myTree = dict()
        for i, parent in enumerate(ppid):
            myTree[parent] = myTree.get(parent, [])
            myTree[parent].append(pid[i])
        queue = [kill]
        res = []
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            queue.extend(myTree.get(cur, []))
        return res
```


stack: 381 ms
```
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        myTree = dict()
        for i, parent in enumerate(ppid):
            myTree[parent] =  myTree.get(parent,[])
            myTree[parent].append(pid[i])
        
        res = []
        stack = [kill]
        while stack:
            cur = stack.pop()
            res.append(cur)
            stack.extend(myTree.get(cur,[]))
            
        return res
```
