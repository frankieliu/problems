
Simple python using dictionary with explaination

https://leetcode.com/problems/maximum-distance-in-arrays/discuss/104618

* Lang:    python3
* Author:  yang_fan
* Votes:   0

First, we save the minimum of each array into min_num dictionary as key and save the maximum of each array into max_num dictionary as key. 
Second, we compare the distance and find the maximum distance.
Third, the key point is the max and min should not come from the same string. We take two steps to avoid this situation: save the array index as the value list, that's why we define the dictionary value as list type :) ; check whether the list are the same or the length of the list larger than 1. In this way, we can make sure that the max and min are not from the same array.
```
def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_num=collections.defaultdict(list)
        max_num=collections.defaultdict(list)
        i=0
        distance=0
        for array in arrays:
            min_num[array[0]].append(i)
            max_num[array[-1]].append(i)
            i+=1
        for i in min_num:
            for j in max_num:
                if (j-i)>distance:
                    if min_num[i]!=max_num[j]:
                        distance=j-i
                    elif len(min_num[i])>1:
                        distance=j-i
        return distance
```
