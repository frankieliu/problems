
easy to understand

https://leetcode.com/problems/validate-stack-sequences/discuss/250177

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
    stack<int> ss;
    int index = 0;
    for(auto& x:pushed){
        ss.push(x);
        while (!ss.empty() and ss.top() == popped[index]) {
            ss.pop();
            index++;
        }
    }
    if(ss.empty())
        return true;
    else
        return false;
    }
};
```
