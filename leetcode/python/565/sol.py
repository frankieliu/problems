
Python solution

https://leetcode.com/problems/array-nesting/discuss/102441

* Lang:    python3
* Author:  wilsonsky18
* Votes:   0

make sure the last element you get is the index that you start.
like ```S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}```, you can find S[**0**] = {5, 6, 2, **0**}
bad code but it works, i get it :(
```
class Solution(object):
    def arrayNesting(self, nums):    
        count , sum_ , n = 1, [] , len(nums)
        for i in range(n):
            temp = i
            if nums[i] != n:
                while 1:
                    if nums[temp] == i:
                        sum_.append(count)
                        nums[temp] = n
                        count = 1
                        break
                    else:
                        temp1 = nums[temp]
                        nums[temp] = n
                        temp = temp1
                        count += 1
        return max(sum_)
```
