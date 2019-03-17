
A complete simulation of the process with explanation (no deque)

https://leetcode.com/problems/dota2-senate/discuss/105864

* Lang:    python3
* Author:  flamesofmoon
* Votes:   0

Change original string into a list `s` of characters so that we could do the following manipulations in the while loop:

1) Find the index `i` of the first Radiant and the index `j` of the first Dire. If we couldn't find the representative of one party, the other party won.

2) 'Kill' the representative with larger index by changing his identity to `X`. 

3) We maintain `s` so that all active representatives are always at the tail part of `s`, so we append the representative with smaller index to the end of the list (which is a one-element left shift of the whole list), leaving increasing amount of junk at the begin of `s` which we don't care. The benefit of doing so is that 
* I don't need to go back and forth as in the real simulations  
* the voting representative is always either `i` or `j` while `i` and `j` simply go rightwards step by step.

Two useful remarks are:
1) The space and time complexities are both O(n) since  `len(s)` is at most 2n.

2) One could easily get rid of the junk at the beginning of `s` by using a deque. 

```
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        s = list(senate)
        i = j = 0
        while True:
            while i < len(s) and s[i] != 'R': # find the next Radiant representative
                i += 1
            if i == len(s):
                return 'Dire'

            while j < len(s) and s[j] != 'D': # find the next Dire representative
                j += 1
            if j == len(s):
                return 'Radiant'

            if i < j:     # after voting, move the voted representative to the end of the list
                s[j] = 'X'
                s.append('R')
            else:
                s[i] = 'X'
                s.append('D')

            i += 1
            j += 1
```
