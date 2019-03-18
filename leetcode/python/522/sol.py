
Python3 simple expression

https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/232627

* Lang:    python3
* Author:  CharlotteGenius
* Votes:   0

def findLUSlength(strs):
    strs.sort(key=len, reverse=True)
    for string1 in strs:
        for l in range(len(string1),0,-1):
            for s in range(len(string1)-l+1):
                sub = string1[s:s+l]
                if all(sub not in x for x in strs if x!=string1):
                    return len(sub)
    return -1

	
