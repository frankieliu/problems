
算法思路整理

https://leetcode.com/problems/unique-paths-iii/discuss/254703

* Lang:    python3
* Author:  chenweigao
* Votes:   0

```py
def uniquePathsIII(self, A):
    self.res = 0
    m, n, empty = len(A), len(A[0]), 1
    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                x, y = (i, j)
            elif A[i][j] == 2:
                end = (i, j)
            elif A[i][j] == 0:
                empty += 1

    def dfs(x, y, empty):
        if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0):
            return
        if (x, y) == end:
            if empty == 0:
                self.res += 1
            return
        A[x][y] = -2
        dfs(x + 1, y, empty - 1)
        dfs(x - 1, y, empty - 1)
        dfs(x, y + 1, empty - 1)
        dfs(x, y - 1, empty - 1)
        A[x][y] = 0
    dfs(x, y, empty)
    return self.res


\'\'\'
\u7B97\u6CD5\u601D\u8DEF\uFF1A
1. \u5148\u7EDF\u8BA1\u7ED9\u5B9A\u6570\u7EC4\u4E2D\u7684\u6570\u7EC4\uFF0C\u786E\u5B9A\u8D77\u70B9\u3001\u7EC8\u70B9\u548C\u53EF\u4EE5\u8BBF\u95EE\u7684\u4E2A\u6570
2. \u66B4\u529Bdfs, \u5206\u60C5\u51B5\u8BA8\u8BBA\uFF1A
    - x, y \u4E0D\u6EE1\u8DB3\u6761\u4EF6\uFF0C\u76F4\u63A5 return
    - \u6570\u7EC4\u503C\u4E0D\u4E3A 0, \u4E0D\u53EF\u8BBF\u95EE\uFF0C\u76F4\u63A5 return
    - \u5982\u679C\u9047\u5230\u7EC8\u70B9\u5E76\u4E14\u6570\u7EC4\u4E2D\u6CA1\u6709\u88AB\u8BBF\u95EE\u7684\u5143\u7D20\uFF0Cres++
3. \u8BB2\u5F53\u524D\u7684 x, y \u6807\u8BB0\u4E3A -2, \u8868\u793A\u5DF2\u8BBF\u95EE
4. \u66B4\u529B dfs \u53EF\u80FD\u7684\u56DB\u4E2A\u70B9
5. \u5C06\u8DEF\u7EBF\u548C\u6807\u8BB0\u6062\u590D\u6210\u4E0A\u4E00\u6B21\u7684\u72B6\u6001
6. \u8FD4\u56DE res
\'\'\'
```
