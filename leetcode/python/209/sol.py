
Python: 3 different AC solutions

https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59294

* Lang:    python3
* Author:  serpol
* Votes:   7

Two pointers:

    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        l = len(nums)
        if not l:
            return 0
        sum = 0
        i = 0
        j = 0
        res = l + 1
        while sum < s:
            sum += nums[j]
            j += 1
            while sum >= s:
                if j - i < res:
                    res = j - i
                sum -= nums[i]
                i += 1
            if j == l:
                break
        if res > l:
            return 0
        return res

Precalculated sums saved at the same list:

    def minSubArrayLen(self, s, nums):
        sm = sum(nums)
        if sm < s:
            return 0
        l = len(nums)
        for i in xrange(l):
            nums[i], sm = sm, sm - nums[i]
        res = l
        nums.append(0)
        for i in xrange(l - 1, -1, -1):
            if nums[i] >= s:
                b = min(l, i + res - 1)
                while nums[i] - nums[b] >= s:
                    res = b - i
                    b -= 1
        return res

Using binary search:

    def minSubArrayLen(self, s, nums):
        sm = sum(nums)
        if sm < s:
            return 0
        l = len(nums)
        for i in xrange(l):
            nums[i], sm = sm, sm - nums[i]
        res = l
        nums.append(0)
        for i in xrange(l - 1, -1, -1):
            e = min(l, i + res - 1)
            while nums[i] - nums[e] >= s:
                if res > e - i:
                    res = e - i
                b = (i + e) / 2
                while nums[i] - nums[b] < s and b < e - 1:
                    b = (b + e) / 2
                if b == e:
                    break
                e = b
        return res

The running time for all three solutions is between 45 - 65 ms.
