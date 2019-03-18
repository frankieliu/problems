
1 line Python solution

https://leetcode.com/problems/h-index/discuss/71055

* Lang:    python3
* Author:  xcv58
* Votes:   13

It's straightforward:

        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
