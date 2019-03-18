
One line solution in Python

https://leetcode.com/problems/majority-element/discuss/51610

* Lang:    python3
* Author:  cigic
* Votes:   101

NOTICE that the majority element **always** exist in the array,so that  the middle **always**  is the answer

    return sorted(num)[len(num)/2]
