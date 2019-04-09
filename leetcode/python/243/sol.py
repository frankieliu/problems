
Python 3 lines solution

https://leetcode.com/problems/shortest-word-distance/discuss/66972

* Lang:    python3
* Author:  bearkino
* Votes:   6

    class Solution(object):
        def shortestDistance(self, words, word1, word2):

            w1 = [i for i in xrange(len(words)) if words[i] == word1]
            w2 = [i for i in xrange(len(words)) if words[i] == word2]

            return min([abs(i - j) for i in w1 for j in w2])

Just use list comprehension to make the code shorter.
