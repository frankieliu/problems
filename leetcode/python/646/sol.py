
Greed is good, greed is right, greed works!

https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/105627

* Lang:    python3
* Author:  iurisrb
* Votes:   0

Enjoy! [Greed is Good speech](https://www.youtube.com/watch?v=MEaJYeRpl1g)
```
def findLongestChain(self, pairs):
    # sort by the second number
    sorted_pairs = sorted(pairs, key=lambda k: k[1])
    # ends_with represents the last seen 'second number'
    i, count, ends_with = 0, 0, float('-infinity')
    while i < len(sorted_pairs):
        pair = sorted_pairs[i]
        start, end = pair
        # search for an interval that starts after the last seen 'second number'
        if ends_with < start:
            ends_with = end
            count += 1
        i += 1
    return count
```
