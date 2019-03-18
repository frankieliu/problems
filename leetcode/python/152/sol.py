
1-line python solution

https://leetcode.com/problems/maximum-product-subarray/discuss/48386

* Lang:    python3
* Author:  danyang3
* Votes:   2

    def maxProduct(self, nums):
        return max(reduce(lambda A, n: [max(A), min(n, A[1]*n, A[2]*n), max(n, A[1]*n, A[2]*n)], nums[1:], [nums[0]]*3))
