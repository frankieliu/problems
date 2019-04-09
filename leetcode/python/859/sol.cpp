
easy to understand

https://leetcode.com/problems/buddy-strings/discuss/257771

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
    bool buddyStrings(string A, string B) {
    if(A.size() != B.size())
        return false;
    vector<pair<char, char>> diff;
    unordered_map<char,int> um;
    for(int i=0;i<A.size();i++){
        if(A[i] != B[i])
            diff.push_back({A[i],B[i]});
        else
            um[A[i]]++;
    }
    if(diff.size() == 2){
        if(diff[0].first == diff[1].second and diff[0].second == diff[1].first)
            return true;
    }
    if(diff.size() == 0){
        for(auto& x:um)
            if(x.second > 1)
                return true;
    }
    return false;
    }
};
```
