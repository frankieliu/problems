In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1060.missing-element-in-sorted-array.algorithms.json

C++ binary search

https://leetcode.com/problems/missing-element-in-sorted-array/discuss/305579

* Lang:    python
* Author:  tangshuo123321
* Votes:   6

```
class Solution {
public:
    int missingElement(vector<int>& nums, int k) {
        int l = 0, h = nums.size();
        while(l < h) {
            int m = l + (h - l) / 2;
            nums[m] - m - k >= nums[0] ? h = m : l = m + 1;
        }
        return nums[0] + l + k - 1;
    }
};
```
