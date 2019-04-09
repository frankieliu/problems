
Java n^2 solution, 116 ms, beats 97.8%

https://leetcode.com/problems/number-of-boomerangs/discuss/92862

* Lang:    java
* Author:  alexilyenko
* Votes:   1

```java
public int numberOfBoomerangs(int[][] points) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int i = 0; i < points.length; i++) {
            // clearing map for new search
            map.clear();
            for (int j = 0; j < points.length; j++) {
                // skipping the same point
                if (i == j) {
                    continue;
                }
                // calculating distance. We will compare distance^2 and get rid of Math.sqrt
                int distance = (points[j][0] - points[i][0])*(points[j][0] - points[i][0]) 
                    + (points[j][1] - points[i][1])*(points[j][1] - points[i][1]);
                // finding number of previously met points with the same distance to i point
                int size = map.getOrDefault(distance, 0);
                // adding that number * 2 to result, since j point can be either second or third point in the bumerang
                count += size++ * 2;
                // adding increased by 1 size back to map
                map.put(distance, size);
            }
        }
        return count;
    }
```
