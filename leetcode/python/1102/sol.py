In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1102.path-with-maximum-minimum-value.algorithms.json

Simple Python Priority Queue Solution

https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/322926

* Lang:    python
* Author:  Merciless
* Votes:   14

Since heappop() only pop the smallest number from the queue, but what I want is the element with the highest score so far, so I change all scores to negative number, so that I can pop the element with highest score. (708 ms)

Notice: memo is used to store the cells that have been visited.
```
class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        de = ((1,0),(0,1),(-1,0),(0,-1))
        rl, cl = len(matrix), len(matrix[0])
        q = [(-matrix[0][0],0,0)]
        memo = [[1 for _ in range(cl)] for _ in range(rl)]
        while q:
            t, x, y = heapq.heappop(q)
            if x == rl - 1 and y == cl - 1:
                return -t
            for d in de:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rl and 0 <= ny < cl and memo[nx][ny]:
                    memo[nx][ny] = 0
                    heapq.heappush(q, (max(t, -matrix[nx][ny]), nx, ny))
```
Update:
Reference to [@davyjing Python Binary Search + DFS](https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/322978/Python-Binary-Search-%2B-DFS) solution, this problem could also be solved though DFS + Greedy approach, which is even slightly faster than my priority queue solution.(692 ms)

For more information about how binary search works here, please see [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
```
class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        de = ((0,1),(1,0),(0,-1),(-1,0))
        rl,cl = len(matrix), len(matrix[0])
        def check(val):
            memo = [[0 for _ in range(cl)] for _ in range(rl)]
            
            def dfs(x,y):
                if x == rl - 1 and y == cl - 1:
                    return True
                memo[x][y] = 1
                for d in de:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx < rl and 0 <= ny < cl and not memo[nx][ny] and matrix[nx][ny] >= val and dfs(nx,ny):
                        return True
                return False
            
            return dfs(0,0)
        
        unique, ceiling = set(), min(matrix[0][0],matrix[-1][-1])
        for i in range(rl):
            for j in range(cl):
                if matrix[i][j] <= ceiling:
                    unique.add(matrix[i][j])
        arr = sorted(unique)
        l, r= 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if check(arr[m]):
                l = m + 1
            else:
                r = m - 1
        return arr[r]
```
                
        

