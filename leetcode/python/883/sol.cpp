
C++, easy and concise solution

https://leetcode.com/problems/projection-area-of-3d-shapes/discuss/253225

* Lang:    cpp
* Author:  naman_nm
* Votes:   0

class Solution {
public:
    int projectionArea(vector<vector<int>>& a) {
        
        int maxi,i,n,j,k,l,m;
        n=a.size();
        if(!n) return 0;
        m=a[0].size();
        k=0;
        for(i=0;i<n;i++)
        {
            maxi=-1;
            for(j=0;j<m;j++)
            {
                if(a[i][j]) k++;
                maxi=max(a[i][j],maxi);
            }
            k+=maxi;
        }
        for(j=0;j<m;j++)
        {
            maxi=-1;
            for(i=0;i<n;i++)
                maxi=max(maxi,a[i][j]);
            k+=maxi;
        }
        return k;
    }
};
