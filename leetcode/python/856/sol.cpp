
easy to understand

https://leetcode.com/problems/score-of-parentheses/discuss/250189

* Lang:    cpp
* Author:  ThinkiNOriginal
* Votes:   0

```
class Solution {
public:
    int scoreOfParentheses(string S) {
    int ans = 0;
    stack<char> ss;
    int power = -1;
    for(int i=0;i<S.size();){
        auto x = S[i];
        if(x == \'(\'){
            ss.push(x);
            power++;
            i++;
        }
        else{
            ans += pow(2,power);
            int j = 0;
            while(S[i+j] == \')\'){
                power--;
                j++;
            }
            i += j;
        }
    }
    return ans;
    }
};
```
