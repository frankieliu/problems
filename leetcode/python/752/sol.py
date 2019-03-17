
Python one end  BFS, two end BFS with optimization and detailed explanation

https://leetcode.com/problems/open-the-lock/discuss/247387

* Lang:    python3
* Author:  pgonarkar
* Votes:   0

**Simple one end BFS**
Maintain simple queue, from start process each element by adding adjacent states into queue. For visited using the the deadends sets itself, no need to using seprate visited set. deadends set act as visited and deadends both.

```
def openLock(self, deadends, target):
 
        deadends = set(deadends)
        start = \'0000\'
        queue = []
        if start not in deadends:
            queue.append(start)
            deadends.add(start)
        ans = 0
        while queue:
            size = len(queue) 
            for i in range(size):
                node = queue.pop(0)
                if node == target:
                    return ans
                states = self.findAllNeighbours(node)
                for state in states:
                    if state not in deadends:
                        deadends.add(state)
                        queue.append(state)
            ans += 1
        
        return -1
    
    def findAllNeighbours(self, node):
        combinations = []
        for i in range(len(node)):
            for j in {-1,1}:
                combinations.append( node[:i] + str((int(node[i])+j) % 10) + node[i+1:])
        return combinations
```

**Two end BFS**
Maintain two sets one from source and one from destination, alternatively processing each of these sets when there is intersection between these two sets return the level

```
def openLock(self, deadends, target):
        deadends = set(deadends) # act as visited and deadends
        begin = \'0000\'
        start, end = set(), set()
        start.add(begin)
        end.add(target)
        ans = 0
        while start and end:
            temp = set()
            for node in start:
                # meeting point of two way BFS
                if node in end:
                    return ans
                if node in deadends:
                    continue
                deadends.add(node)
                states = self.findAllNeighbours(node)
                for state in states:
                    if state not in deadends:
                        temp.add(state)
			# swap the two sets
			# optimization : swap sets based on length, keep start set always smaller  
            start = end
            end = temp
            ans += 1
        return -1
    
    def findAllNeighbours(self, node):
        combinations = []
        for i in range(len(node)):
            for j in {-1,1}:
                combinations.append( node[:i] + str((int(node[i])+j) % 10) + node[i+1:])
        return combinations
```
