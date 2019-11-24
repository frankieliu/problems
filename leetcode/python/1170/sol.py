In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1170.compare-strings-by-frequency-of-the-smallest-character.algorithms.json

[Python] 2-liner

https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/discuss/366927

* Lang:    python
* Author:  cenkay
* Votes:   20

* min(w) will give smallest character for each word \'w\' in \'words\' list
* w.count(min(w)) will give frequency of smallest character for each word \'w\' in \'words\' list
* \'f\' is the sorted frequency list of \'words\'
* For each query \'q\' in \'queries\' list, we find its rightmost suitable index in the frequency \'f\' list
* Total length of frequency list \'f\' minus index will give answer[i]
* Index is determined by bisect module, which gives number of words having frequency of their smallest character less than or equal to query \'q\'
```
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]
```
