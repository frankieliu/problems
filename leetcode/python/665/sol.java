
Simple O(n) Java solution 9ms with comments

https://leetcode.com/problems/non-decreasing-array/discuss/239286

* Lang:    java
* Author:  mjain123
* Votes:   2

```
class Solution {
    public boolean checkPossibility(int[] nums) {        
        int count = 1; // can be modified to number of modifications allowed. current case = 1
        for (int i=0;i<nums.length-1;i++) {
            if (nums[i] <= nums[i+1]) {
                continue;
            }
            if (count>0) {
                count--;
                if (i==0) {
                    continue;
                }
                // eg case [ 1, 4, 2, 3], for i = 1, 2 > 1, change 4 to 1
                if(nums[i+1] >= nums[i-1]) {
                    nums[i] = nums[i-1];
                }
                // eg case [ 2, 3, 5, 2, 8], for i = 2, 2 < 3, change 2 to 5
                else {
                    nums[i+1] = nums[i];
                }
            }
            else {
                return false;
            }
        }
        return true;
    }
}
```

The key here is - 
for the fail case - nums[i] > nums[i+1], determine if we need to change nums[i] to nums[i-1] or change nums[i+1] to nums[i]
