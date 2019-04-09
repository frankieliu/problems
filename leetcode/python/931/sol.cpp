
C++ DP solution 98%

https://leetcode.com/problems/minimum-falling-path-sum/discuss/248862

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

```
class Solution {

public:
    int minFallingPathSum(vector<vector<int>>& A) {

        for (auto i = 1; i < A.size(); i++) {
            for (auto j = 0; j < A[i].size(); j++) {
                if (j == 0)
                    A[i][j] += min(A[i - 1][j], A[i - 1][j + 1]);
                else if (j == A[i].size() - 1)
                    A[i][j] += min(A[i - 1][j], A[i - 1][j - 1]);
                else
                    A[i][j] += min(A[i - 1][j - 1], min(A[i - 1][j], A[i - 1][j + 1]));
                
            }
        }
        
        int tmp = A.back()[0];
        for (auto i = 0; i < A.back().size(); i++) {
            if (tmp > A.back()[i])
                tmp = A.back()[i];
        }
        
        return tmp;
    }
};
```
