
C++ solution (100%)

https://leetcode.com/problems/reordered-power-of-2/discuss/250192

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

```
class Solution {
public:
    bool reorderedPowerOf2(int N) {
        
        for (auto i = 0; i < 30; i++) {
            auto target = 1 << i;
            auto tmp = target;
            int cnt[10] = {0};
            
            while (tmp > 0) {
                cnt[tmp % 10]++;
                tmp /= 10;
            }
            
            tmp = N;
            while (tmp > 0) {
                if (--cnt[tmp % 10] < 0)
                    break;

                tmp /= 10;
            }
            if (tmp > 0)
                continue;
            
            tmp = 0;
            for (auto j = 0 ; j < 10; j++)
                tmp += cnt[j];

            if (tmp == 0)
                return true;
        }
        return false;
    }
};
```
