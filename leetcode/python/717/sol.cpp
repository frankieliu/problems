
Simple 3 lines C++

https://leetcode.com/problems/1-bit-and-2-bit-characters/discuss/108982

* Lang:    cpp
* Author:  zefengsong
* Votes:   0

```
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0, n = bits.size();
        while(i < n - 1) i += bits[i] + 1;
        return i != n;
    }
};
```
