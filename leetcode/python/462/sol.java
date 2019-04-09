
4 lines Java Solution

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94985

* Lang:    java
* Author:  fabrizio3
* Votes:   1

```
Arrays.sort(nums);
int i=0, j=nums.length-1, moves = 0;
while(i<j) moves+=nums[j--]-nums[i++];
return moves;
```
