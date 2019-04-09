
ugly solution works

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/257769

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:

int changeCounts(vector<int>& A,vector<int>& B){
    if(A == B)
        return 0;
    if(A.size() == 1)
        return 0;
    int target = A[0];
    int ansA = 0;
    for(int i=1;i<A.size();i++){
        if(A[i] != target and B[i] == target)
            ansA++;
        else if(A[i] != target and B[i] != target){
            ansA = INT_MAX;
            break;
        }
    }
    target = B[0];
    int ansB = 0;
    for(int i=0;i<A.size();i++){
        if(A[i] != target and B[i] == target)
            ansB++;
        else if(A[i] != target and B[i] != target){
            ansB = INT_MAX;
            break;
        }
    }
    
    return min(ansA,ansB);
}

int minDominoRotations(vector<int>& A,vector<int>& B){
    int ca = changeCounts(A, B);
    int cb = changeCounts(B, A);
    if(ca == INT_MAX and cb == INT_MAX)
        return -1;
    else if(ca == INT_MAX)
        return cb;
    else if(cb == INT_MAX)
        return ca;
    return min(ca,cb);
}
};
```
