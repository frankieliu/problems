
Python: solution with strings

https://leetcode.com/problems/total-hamming-distance/discuss/232703

* Lang:    python3
* Author:  neopug
* Votes:   0

Thans guys for all your solutions, there are a lot of interesting variants but I tryied to reinvent wheel by myself.
```
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        if nums == []:
            return 0
        nums_len = len(nums)
        for i in range(nums_len):
            for n in range (i+1,nums_len):
                result += bin(nums[i]^nums[n]).count(\'1\')
        return result
```

Unfortunately this solution is faling with Time Limit Exceeded on 36/47 test (10k items). I could suggest that `.count(\'1\')` operation is taking too much time but I have no idea how to optimize it to pass all the tests. 
I will be very appriciated for any suggestion how to optimize that solution (when we\'re XORing two numbers).
Best regards,
Maks
