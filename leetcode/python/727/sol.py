
Python O(M*N) solution TLE, same algo in C accepted

https://leetcode.com/problems/minimum-window-subsequence/discuss/109364

* Lang:    python3
* Author:  erjoalgo
* Votes:   1

Python O(M*N) solution not accepted, but the same exact algorithm in C is accepted:

Python (TLE):

```
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        mna=-1
        mnb=len(S)
        dp = [[-1 for _ in xrange(len(T))] for __ in xrange(len(S))]
        
        for s in xrange(len(S)):
            for t in xrange(len(T)):
                idx = -1
                if s>0:
                    idx = dp[s-1][t]
                if S[s]==T[t]:
                    if t==0:
                        idx = s
                    elif s>0:
                        idx = dp[s-1][t-1]
                dp[s][t] = idx
            a = dp[s][-1]
            b = s+1
            if a!=-1 and b-a < mnb -mna:
                mna = a
                mnb = b
        return "" if mna == -1 else S[mna:mnb]
```


C:

```
char* minWindow(char* S, char* T) {
    int tLen = strlen(T);
    int sLen = strlen(S);
    
    int dp[sLen][tLen];
    memset(dp, -1, sizeof(dp));
    
    int mna=-1;
    int mnb=sLen;
    for (int s=0;s<sLen;s++){
        for (int t=0;t<tLen;t++){
            int idx=-1;
            if (s-1>=0)
                idx = dp[s-1][t];
            if (S[s]==T[t]){
                if (t==0)
                    idx=s;
                else if (s-1>=0)
                    idx = dp[s-1][t-1];
            }
            dp[s][t]=idx;
        }

        int a = dp[s][tLen-1];
        int b = s+1;        
        
        if (a>=0 && b-a < mnb-mna){
            mnb=b;
            mna=a;
        }
    }
    if (mna==-1){
        return "";
    }else{
        S[mnb]=0;
        return S+mna;
    }
    
}
```

What's the point of providing Python as an option?
