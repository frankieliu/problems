
O(1) Python solution with cheat sheet :P

https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83086

* Lang:    python3
* Author:  MingHan1990
* Votes:   3

    cheat_sheet = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771]
    class Solution(object):
        def countNumbersWithUniqueDigits(self, n):
            return cheat_sheet[n] if n<11 else cheat_sheet[10]
