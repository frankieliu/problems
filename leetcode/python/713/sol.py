
straightforward two-pointer python O(n) solution

https://leetcode.com/problems/subarray-product-less-than-k/discuss/108831

* Lang:    python3
* Author:  ayalinda
* Votes:   1

        status = (1, 0) # (product of elements in window, left window)
        result = 0
        for i, num in enumerate(nums):
            product, left = status
            product *= num
            while product >= k and left < i+1:
                product /= nums[left]
                left += 1
            status = (product, left)
            result += i - left + 1          
        return result
