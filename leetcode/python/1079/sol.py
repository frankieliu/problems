In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1079.letter-tile-possibilities.algorithms.json

Concise java solution

https://leetcode.com/problems/letter-tile-possibilities/discuss/308284

* Lang:    python
* Author:  mo39-fmbh
* Votes:   85

```
    public int numTilePossibilities(String tiles) {
        int[] count = new int[26];
        for (char c : tiles.toCharArray()) count[c - \'A\']++;
        return dfs(count);
    }
    
    int dfs(int[] arr) {
        int sum = 0;
        for (int i = 0; i < 26; i++) {
            if (arr[i] == 0) continue;
            sum++;
            arr[i]--;
            sum += dfs(arr);
            arr[i]++;
        }
        return sum;
    }
```

**Thoughts**

input: AAB
count: A -> 2, B -> 1

For sequence of length 1:
* 	We can pick either A, or B.
* 	So we have "A", "B".
	
For sequence of length 2:
* 	We build it based on "sequence of length 1"
* 	For "A":
	* 	count: A -> 1, B -> 1
	*	We can still pick either A, or B
	*	So we have "AA", "AB"
*	For "B":
	*	count: A -> 2, B -> 0
	*	We can only pick A
	*	So we have "BA"
		
For sequence of length 3: blablabla

**Implementation**
1. We don\'t need to keep track of the sequence. We only need count
2. If we implement the above idea by each level (Count all sequence of length 1, then count all sequence of length 2, etc), we have to remember previous sequence.
3. So we use recursion instead. Just remember to add the count back (`arr[i]++`).

