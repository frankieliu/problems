
Think conversely, max poisoned time - not poisoned time

https://leetcode.com/problems/teemo-attacking/discuss/97582

* Lang:    java
* Author:  Johnny9L
* Votes:   0

The max poisoned time is: last attack + duration - first attack
Possible Ashe's clear states: timeSeries[i] - timeSeries[i-1] - duration
O(n) solution in Java:
```
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (duration==0 || timeSeries.length==0) return 0;
        int n = timeSeries.length;
        int total = timeSeries[n-1]+duration-timeSeries[0];
        for (int i=1; i<n; ++i) {
            int d = timeSeries[i] - timeSeries[i-1];
            if (d>duration)
                total -= (d-duration);
        }
        return total;
    }
````
