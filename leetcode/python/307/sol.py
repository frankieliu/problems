
"0 lines" Python

https://leetcode.com/problems/range-sum-query-mutable/discuss/75802

* Lang:    python3
* Author:  StefanPochmann
* Votes:   37

    class NumArray(object):
        def __init__(self, nums):
            self.update = nums.__setitem__
            self.sumRange = lambda i, j: sum(nums[i:j+1])

I added two lines, but I also removed two lines, so zero overall, right? Just kidding :-P

Not a serious solution, just showing some Python trickery. The `sumRange` takes linear time, but due to the test suite being weak, this solution gets accepted (in about 1200-1300ms).
