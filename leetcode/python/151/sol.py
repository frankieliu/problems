
My Accept Answer of Python with one line

https://leetcode.com/problems/reverse-words-in-a-string/discuss/47726

* Lang:    python3
* Author:  Lendfating
* Votes:   27

My Python code using the function of array and string. Both time and memory is O(n).

    class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
