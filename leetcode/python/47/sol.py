
Iterative Python solution without using set, 111ms

https://leetcode.com/problems/permutations-ii/discuss/18657

* Lang:    python3
* Author:  clue
* Votes:   24

Duplication happens when we insert the duplicated element before and after the same element, to eliminate duplicates, just insert only after the same element.

    
    def permuteUnique(self, num):
        if not num:
            return []
        num.sort()
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret
