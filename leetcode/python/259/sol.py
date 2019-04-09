
11 lines O(n^2) Python

https://leetcode.com/problems/3sum-smaller/discuss/68818

* Lang:    python3
* Author:  StefanPochmann
* Votes:   41

After sorting, if `i, j, k` is a valid triple, then `i, j-1, k`, ..., `i, i+1, k` are also valid triples. No need to count them one by one.

    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        return count
