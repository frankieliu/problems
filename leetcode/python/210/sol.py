
Python dfs, bfs solutions with comments.

https://leetcode.com/problems/course-schedule-ii/discuss/59321

* Lang:    python3
* Author:  caikehe
* Votes:   51

     
    # BFS
    def findOrder1(self, numCourses, prerequisites):
        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []
        
    # DFS
    def findOrder(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []
