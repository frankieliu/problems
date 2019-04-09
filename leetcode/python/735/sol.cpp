
using stack,20ms, easy to understand

https://leetcode.com/problems/asteroid-collision/discuss/253977

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
            stack<int> s;
    for(auto& x:asteroids){
        if(s.empty())
            s.push(x);
        else{
            if(x<0 and s.top() > 0){
                bool exist = false;
                while (!s.empty() and s.top()>0) {
                    if(s.top() < -x){
                        s.pop();
                        exist = true;
                    }
                    else if(s.top() > -x){
                        exist = false;
                        break;
                    }
                    else{
                        s.pop();
                        exist = false;
                        break;
                    }
                }
                if(exist)
                    s.push(x);
            }
            else
                s.push(x);
        }
    }
    vector<int> ans;
    while (!s.empty()) {
        ans.push_back(s.top());
        s.pop();
    }
    reverse(ans.begin(),ans.end());
    return ans;
    }
};
```
