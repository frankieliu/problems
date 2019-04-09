
Optimized Python Solution using Trie Tree and Merge Intervals

https://leetcode.com/problems/bold-words-in-string/discuss/247076

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

Here are two key points: 
1. **Trie Tree** is used to speed up string match (faster than **find** or **startwith** in large query request).
2. Using **Merge Intervals** instead of **mask** to reduce Time and Space Complexity, both from O(n) to O(m), **m** represets interval numbers after merged.

```
class Solution:
    def boldWords(self, words: \'List[str]\', S: str) -> str:
        trie, n, intervals, res = {}, len(S), [], ""

        # create trie tree
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = 0

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, max_end = trie, None
            for j in range(i, n):
                if S[j] not in cur:
                    break
                cur = cur[S[j]]
                if "#" in cur:
                    max_end = j + 1
			# just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += S[prev_end:start] + \'<b>\' + S[start:end] + "</b>"
            prev_end = end
        return res + S[prev_end:]
```

inspired by 
https://leetcode.com/problems/bold-words-in-string/discuss/155076/Python-understandable-trie-and-set-solution
https://leetcode.com/problems/bold-words-in-string/discuss/113102/Python-Simple-Solution-Using-Merge-Intervals
