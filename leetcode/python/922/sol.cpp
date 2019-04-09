
C++, easy O(n) time in-place solution

https://leetcode.com/problems/sort-array-by-parity-ii/discuss/253500

* Lang:    cpp
* Author:  naman_nm
* Votes:   0

class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& a) {
        
        int i,j=1,n=a.size();
        for(i=0;i<n;i+=2)
        {
            if(a[i]%2)
            {
                while(a[j]%2)
                    j+=2;
                swap(a[i],a[j]);
            }   
        }
        return a;
    }
};
