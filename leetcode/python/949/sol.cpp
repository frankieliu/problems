
backtracking , easy to understand

https://leetcode.com/problems/largest-time-for-given-digits/discuss/254078

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
void bt(vector<int>& A,vector<bool>& used,string cur_time,string& ans){
    if(cur_time.size() == A.size()){
        if(cur_time[0] == \'2\' and cur_time[1]<=\'3\' and cur_time[2]<=\'5\' and cur_time[3]<=\'9\')
            ans = max(ans,cur_time);
        else if(cur_time[0]<=\'1\' and cur_time[1]<=\'9\' and cur_time[2]<=\'5\' and cur_time[3]<=\'9\')
            ans = max(ans,cur_time);
    
    }
    else{
        for(int i=0;i<A.size();i++){
            if(!used[i]){
                used[i] = true;
                cur_time = cur_time + to_string(A[i]);
                bt(A,used,cur_time,ans);
                cur_time.erase(cur_time.size()-1,1);
                used[i] = false;
            }
        }
    }
}

string largestTimeFromDigits(vector<int>& A){
    vector<bool> used(A.size(),false);
    string time;
    string ans;
    bt(A,used,time,ans);
    if(ans.size() == 0)
        return ans;
    ans.insert(2,":");
    return ans;
}
};
```
