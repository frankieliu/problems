
Java solution with extra space

https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/243342

* Lang:    java
* Author:  amogh3
* Votes:   0

```class Solution {
    public List<Integer> findDuplicates(int[] nums) 
    {
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
        List<Integer> l = new ArrayList<Integer>();
        for(int i:nums){
            if(hm.containsKey(i)){
                l.add(i);
            }
            else{
                hm.put(i,1);
            }
        }
        return l;
    }
}```
