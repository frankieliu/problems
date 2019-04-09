
Python one-liner

https://leetcode.com/problems/sort-transformed-array/discuss/83320

* Lang:    python3
* Author:  StefanPochmann
* Votes:   9

Because the input is sorted and the function is a second degree polynomial, simply applying the function will result in at most two increasing/decreasing runs. Which [Python's sort function](https://en.wikipedia.org/wiki/Timsort) will recognize and simply reverse/merge in O(n).

    def sortTransformedArray(self, nums, a, b, c):
        return sorted(a*x*x + b*x + c for x in nums)
