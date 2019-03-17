
Radix Sort in Python

https://leetcode.com/problems/maximum-gap/discuss/50709

* Lang:    python3
* Author:  selfboot
* Votes:   2

    
    class Solution(object):
    """
    Radix sort, you can see the explanation follow the links.
    https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
    """
    def maximumGap(self, nums):
        if not nums:
            return 0

        max_num = max(nums)
        bucket = [[] for i in range(10)]
        exp = 1
        while max_num / exp > 0:
            for num in nums:
                bucket[(num/exp) % 10].append(num)
            nums = []
            for each in bucket:
                nums.extend(each)
            bucket = [[] for i in range(10)]
            exp *= 10

        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap
