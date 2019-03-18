
Python Easy O(n) Solution

https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995

* Lang:    python3
* Author:  girikuncoro
* Votes:   115

Start with the maximum numbers for the first and second element. Then:
(1) Find the first smallest number in the 3 subsequence
(2) Find the second one greater than the first element, reset the first one if it's smaller

    def increasingTriplet(nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
