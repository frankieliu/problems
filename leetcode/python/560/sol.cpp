
C++ solution 99%

https://leetcode.com/problems/subarray-sum-equals-k/discuss/251202

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

Base on the property `sum(i,j) = sum(0,j) - sum(0,i)`, we create an hash map to record every `sum(0,i)`.
For each new `j` when travesing the input array, check the the map which store the information of `sum(0,i), i < j`.
If `map[sum(0,j) - k]` exist, means there are` sum(0,j) - sum(0,i)` eqauls `k`.
Then update the count.

```
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        auto sum = 0;
        auto cnt = 0;
        unordered_map<int, int> m;
        m[0] = 1;

        for (auto i = 0; i < nums.size(); i++) {
            sum += nums[i];

            if (m.find(sum - k) != m.end())
                cnt += m[sum - k];

            m[sum]++;
        }

        return cnt;
    }
};
```
