
6-liner O(N*logk) time, optimized space O(k) (NOT fixed range!)

https://leetcode.com/problems/delete-and-earn/discuss/109883

* Lang:    cpp
* Author:  zzg_zzm
* Votes:   0

Even though the integer `nums[i]` has range `[1, 10000]`, the following code deals without range restriction.

The key is to use a `std::map` to store sums of only distinct values (instead of array allocation of max range `10000` regardless whether a value shows up in the range).

The DP process is similar to [House Robber](https://leetcode.com/problems/house-robber), but we need to check whether two keys in map `sum` are adjacent, i.e., `i->first == prev(i)->first+1` for each iterator `i`. 

**NOTE:**
* The DP equation is same as [House Robber](https://leetcode.com/problems/house-robber) only for adjacent keys.
* Only need `O(k)` space (`k = ` number of distinct values in `nums`)
* No need to keep all DP results since the recursion order is just `2`.


```cpp
    int deleteAndEarn(vector<int>& nums) 
    {
        // get sum for each distinct non-zero value
        map<int, int> sum;
        for (int num : nums) if (num) sum[num] += num;
        
        // initial values for DP
        int res0 = 0, res1 = 0, res = sum.begin()->second;
        
        for (auto i = sum.begin()++; i != sum.end(); i++, res0 = res1, res1 = res)     
            res = (i->first == prev(i)->first+1)? max(res1, res0 + i->second) : res1 + i->second;

        return res;        
    }
```
