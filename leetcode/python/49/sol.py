
5-line Python solution, easy to understand

https://leetcode.com/problems/group-anagrams/discuss/19202

* Lang:    python3
* Author:  kitt
* Votes:   47

    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
