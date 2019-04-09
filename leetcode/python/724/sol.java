
Eh, 10000 is small [Accepted]

https://leetcode.com/problems/find-pivot-index/discuss/109263

* Lang:    java
* Author:  JavaProgrammer21
* Votes:   0

Worst case: (10,000)^2 = 100,000,000

Assuming 2 billion actions per second (easily achieveable on intel core i5), the worst case is 500 ms

Indeed, this code runs in 571 ms
```
class Solution {
    //Find partial sum between start inclusive and stop exclusive
    public int sum(int[] nums, int start, int stop){
        int ret = 0;
        for(int i = start; i < stop; i++){
            ret += nums[i];
        }
        return ret;
    }
    public int pivotIndex(int[] nums) {
        //Iterate through array positions: O(n^2)
        for(int i = 0; i < nums.length; i++){
            if(sum(nums, 0, i) == sum(nums, i + 1, nums.length)){
                return i;
            }
        }
        //If not found, return -1
        return -1;
    }
}
```
