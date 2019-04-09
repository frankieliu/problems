
AC Python one line 44 ms solution

https://leetcode.com/problems/flip-game/discuss/73946

* Lang:    python3
* Author:  dietpepsi
* Votes:   9

    def generatePossibleNextMoves(self, s):
        return [s[:i] + "--" + s[i + 2:] for i in xrange(len(s) - 1) if s[i:i + 2] == '++']


    # 25 / 25 test cases passed.
    # Status: Accepted
    # Runtime: 44 ms


It is a simple list comprehension and a filter
