
Efficient Java solution

https://leetcode.com/problems/brick-wall/discuss/245403

* Lang:    java
* Author:  joe911
* Votes:   0

``` java
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int max= Integer.MIN_VALUE;
        int n = wall.size();
        if(n==0 ) return 0;
        //(key,value): key=width/dist from left where a brick ends, value=number of times it is accessed i.e. a brick ends there
        HashMap<Integer,Integer> map = new HashMap<>();
        List<Integer> x1= wall.get(0);
        int width=0;
        for(Integer a1:x1)
            width+=a1;
        for( List<Integer> x:wall)
        {
            int curr=0;
            for(Integer a:x)
            {
            curr+=a;
            if(curr!=width)
            map.put(curr,map.getOrDefault(curr,0)+1);
            }
        }
        if (map.keySet().size() ==0) return n;
        for(Integer i:map.keySet())
             max=Math.max(max,map.get(i)); 
    return (n-max);
    }
}
```
