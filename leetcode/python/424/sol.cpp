
C++ Solution using two pointers with O(n) time complexity and O(1) space

https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91316

* Lang:    cpp
* Author:  yular
* Votes:   0

```
class Solution {
public:
    int characterReplacement(string s, int k) {
        int ans = 0, n = s.size(), cnt = 0, fidx = 0;
        if(n == 0)
            return ans;
        vector<bool> vis(26, false);
        int idx = 0;
        for(int i = 0; i < n; ++ i){
            idx = s[i] - 'A';
            vis[idx] = 1;
        }
        char ch = 0;
        for(int c = 0; c < 26; ++ c){
            if(!vis[c])
                continue;
            cnt = k;
            ch = 'A' + c;
            fidx = -1;
            for(int i = 0; i < n; ++ i){
                if(s[i] != ch)
                    -- cnt;
                while(fidx < i && cnt < 0){
                        if(s[++ fidx] != ch)
                            ++ cnt;
                }
                if(cnt >= 0)
                    ans = max(ans, i - fidx);
            }
        }
        return ans;
    }
};
```
