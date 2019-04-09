
PYTHON - 36 ms - %100 - With Explanation

https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234821

* Lang:    python3
* Author:  tiryaki
* Votes:   0

The idea is simple.

In PART 1 (commented on the code)
1. If two variables are equal, add variables into the same set. If their nodes are different, merge their sets
2. If they are not equal, add the equation into `check` list to control at the end of the dictionary built

In PART 2
Now, let\'s check if inequalities in `check` list are satisfied with the current structure:

1. check if two variables are equal 
2. check if two variables exist in the dictionary and they refer to same variable
3. If these `1` and `2` conditions are true, then there is an inconsistency. Return `False`

If all `check` conditions pass, return `True`
```
class Node:
    def __init__(self, x):
        self.s = {x}

    def merge(self, n):
        self.s = self.s.union(n.s)
        n.s = self.s
        
class Solution:
    def equationsPossible(self, equations: \'List[str]\') -> \'bool\':
        vmap = {}
        
        check = []
        # PART 1
        for e in equations:
            if e[1] != \'=\':
                check.append(e)
                continue
                
            x = e[0]
            y = e[-1]
            
            if x in vmap and y in vmap:
                res = vmap[x].merge(vmap[y])
            elif x in vmap:
                add_alias(vmap, x, y)
            elif y in vmap:
                add_alias(vmap, y, x)
            else:
                vmap[x] = Node(x)
                add_alias(vmap, x, y)
         
		# PART 2
        for e in check:
            x = e[0]
            y = e[-1]
            if x == y or (x in vmap and y in vmap[x].s ) or (y in vmap and x in vmap[y].s):
                return False
            
        return True
                    
def add_alias(vmap, v1, v2):
    vmap[v1].s.add(v2)
    vmap[v2] = vmap[v1]
```
