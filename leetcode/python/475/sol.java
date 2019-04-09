
Java Easy Solution with Explanation

https://leetcode.com/problems/heaters/discuss/95983

* Lang:    java
* Author:  snowcat
* Votes:   1

The basic idea is that, for every house location in the `houses` array, we try to locate the positions of the heaters right before and after this house, and calculate the distances.

```
public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);
        
        // pre represents the heater that's ahead of the current house
        int pre = heaters[0];
        // index of the heater
        int i = 0;
        int res = 0;
        for (int house : houses) {
            // looking for the heater that's immediately after the current house
            while (i < heaters.length - 1 && heaters[i] < house) {
                pre = heaters[i];
                i++;
            }
            
            int distanceToPreHeater = Math.abs(house - pre);
            int distanceToAfterHeater = Math.abs(house - heaters[i]);
            res = Math.max(res, Math.min(distanceToPreHeater, distanceToAfterHeater));
        }
        
        return res;
    }
}
```
