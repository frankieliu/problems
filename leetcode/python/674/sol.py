
Simple and Easy-to-Understand C++/Python Solution

https://leetcode.com/problems/longest-continuous-increasing-subsequence/discuss/107362

* Lang:    python3
* Author:  yang_fan
* Votes:   0

C++
```
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        int count=1;
        int res=1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]>nums[i-1]){
                count++;
                res=max(count,res);
            }
            else{
                res=max(count,res);
                count=1;
            }
        }
    return res;
    }
};
//36 / 36 test cases passed.
//Status: Accepted
//Runtime: 13 ms
```
Python
```
class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:return 0
        count=1
        res=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
                res=max(count,res)                
            else:
                res=max(count,res)
                count=1
        return res
#36 / 36 test cases passed.
#Status: Accepted
#Runtime: 45 ms
```
