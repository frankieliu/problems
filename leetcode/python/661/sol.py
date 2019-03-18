
Straightforward solution in Python

https://leetcode.com/problems/image-smoother/discuss/106624

* Lang:    python3
* Author:  QM_12
* Votes:   0

```
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[1] * len(M[0]) for _ in range(len(M))]

        for row in range(len(M)):
            for col in range(len(M[0])):
                d = [-1, 0, 1]

                vad_m = [M[row + r][col + c] \\
                         for r in d \\
                         for c in d \\
                         if 0 <= row + r <= len(M) - 1 and \\
                         0 <= col + c <= len(M[0]) - 1]

                avg = int(sum(vad_m) / len(vad_m))

                res[row][col] = int(avg)
        return res
```

BTW,  be careful with the initialization of `list of list` in python!
Eg.
If:
`a = [[0] * 3] * 3`
when assignment:
`a[0][0] = 1`
we obtain
```
a:
[[1, 0, 0],
[1, 0, 0],
[1, 0, 0]]
```
instead of 
```
a:
[[1, 0, 0],
[0, 0, 0],
[0, 0, 0]]
```
