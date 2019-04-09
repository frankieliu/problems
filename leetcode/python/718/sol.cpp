
C++ simple DP solution

https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/253502

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

It\'s a O(mn) solution.
Basic idea is create a matrix `M` and store the max length of repeated subarray which end with `A[i]` or `B[j]` in `M[i][j]`.
For example
```
A: [1,2,3,2,1]
B: [3,2,1,4,7]
```
Make the below matrix and then find the maximum value in it.
```
     3   2   1   4   7
1   [0] [0] [1] [0] [0]
2   [0] [1] [0] [0] [0]
3   [1] [0] [0] [0] [0]
2   [0] [2] [0] [0] [0]
1   [0] [0] [3] [0] [0]
```
```
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int res = 0;
        vector<vector<int>> v(A.size(), vector<int>(B.size(), 0));
        for (auto i = 0; i < A.size(); i++) {
            for (auto j = 0; j < B.size(); j++) {
                if (A[i] == B[j]) {
                    if (i == 0 || j == 0)
                        v[i][j] = 1;
                    else
                        v[i][j] = v[i - 1][j - 1] + 1;
                    
                    res = max(res, v[i][j]);
                }
            }
        }
        
        return res;
    }
};
```
