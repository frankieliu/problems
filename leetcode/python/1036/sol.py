In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1036.escape-a-large-maze.algorithms.json

python solution with picture show my thoughts

https://leetcode.com/problems/escape-a-large-maze/discuss/282870

* Lang:    python
* Author:  bupt_wc
* Votes:   43

a very interesting problem!

At first, I thought that this problem was to construct a closed interval with points in blocked and all boundary points (4\\*10^6 points), 
and then look at the location of the source and target.

then, I draw some cases that shows below

![image](https://assets.leetcode.com/users/2017111303/image_1556424333.png)

there are two cases that source node cannot reach target node
`case 1` is the blocked points and boundary points form a closed interval and one node(source or target) in,another out.
`case 2` is only the blocked points form a closed interval and one node(source or target) in,another out.

`the key point is the length of blocked is smaller than 200`, so the closed area will not too large
we can just use bfs to search from the source, and set a maximum step.
after moving maximum step, if we can still move, then it must can reach the target point

here the maximum step should be `the length of blocked`, seen in case 3
of course, we should handled the different situation with the starting node
```python
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: return True
        blocked = set(map(tuple, blocked))
        
        def check(blocked, source, target):
            si, sj = source
            ti, tj = target
            level = 0
            q = collections.deque([(si,sj)])
            vis = set()
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    if i == ti and j == tj: return True
                    for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if 0<=x<10**6 and 0<=y<10**6 and (x,y) not in vis and (x,y) not in blocked:
                            vis.add((x,y))
                            q.append((x,y))
                level += 1
                if level == len(blocked): break
            else:
                return False
            return True
        
        return check(blocked, source, target) and check(blocked, target, source)
```
