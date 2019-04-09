
Python solution (linear time, and linear space) with dummies explanation

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77801

* Lang:    python3
* Author:  laser
* Votes:   1

``` 
# linear time, and linear space complexity
def maxSubArrayLen(self, nums, k):
    if not nums:
        return 0
    prefix_sums = [0]
    number_sum = 0
    # generate a list of the prefix sums
    for i in range(len(nums)):
        number_sum += nums[i]
        prefix_sums.append(number_sum)
    ht = {}
    max_length = 0
    for i in range(len(prefix_sums)):
        # We want the first (left-most) instance of a sum because we are looking
        # for the longest length subarray
        if prefix_sums[i] not in ht:
            ht[prefix_sums[i]] = i
        # If a previously seen sum that equates to a difference of k, then determine
        # if it is the longest subarray length
        if (prefix_sums[i] - k) in ht:
            max_length = max(max_length, i - ht[prefix_sums[i]-k])
    return max_length
```
Explanation:
I'll explain the algorithm using the following example:
input nums = [-2, 7, 1,-1, 5,-2, 3]
prefix_sums = [0,-2, 5, 6, 5,10, 8,11]
At curr_index 7 in the prefix_sums list, the sum from the beginning to curr_index is 8, and if you subtract 8 with the target of 3 then you get 5. From that we are looking for an index to the left of curr_index that equates to that 5. To the left of curr_index because whatever index we find represents at that specific point in time, that was the sum. If you do find that index to the left of curr_index that is equal to 5, then you have found two indexes that have changed a difference of 3 (target) and therefore have sumed to 3. then the difference between the indexes represents the length of that subarray.

This is using the [prefix sum algorithm](https://en.wikipedia.org/wiki/Prefix_sum) to achieve the linear time complexity.
