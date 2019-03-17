
A two-line Python solution, 176 ms

https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/77029

* Lang:    python3
* Author:  kitt
* Votes:   7

Since we only deal with 26 lower case letters, a mask can be used to check whether two words share common letters or not. Use a dictionary to record the max word length of each mask. 348 ms, beats 99.76% of Python submissions. 

    class Solution(object):
        def maxProduct(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            maskLen = {reduce(lambda x, y: x | y, [1 << (ord(c) - 97) for c in word], 0): len(word) 
                for word in sorted(words, key = lambda x: len(x))}.items()
            return max([x[1] * y[1] for i, x in enumerate(maskLen) for y in maskLen[:i] if not (x[0] & y[0])] or [0])
