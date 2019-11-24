In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1150.check-if-a-number-is-majority-element-in-a-sorted-array.algorithms.json

Java just one binary search O(logN)), 0ms, beats 100%

https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/discuss/358130

* Lang:    python
* Author:  kmw
* Votes:   4

```
class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int firstIndex = firstOccur(nums, target);
        int plusNBy2Index = firstIndex + nums.length/2;
        
        if (plusNBy2Index<nums.length 
            && nums[firstIndex] == target
            && nums[plusNBy2Index] == target) {
            return true;
        }
        
        return false;
    }
    
    private int firstOccur(int[] nums, int target) {
        int low = 0;
        int high = nums.length;
        while (low < high) {
            int mid = low + (high-low)/2;
            if (nums[mid] < target) low = mid + 1;
            else if (nums[mid] >= target) high = mid;
        }
        return low;
    }
    
}
```
