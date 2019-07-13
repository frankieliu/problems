In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1062.longest-repeating-substring.algorithms.json

easy to understand N^2 solution

https://leetcode.com/problems/longest-repeating-substring/discuss/303884

* Lang:    python
* Author:  JagdishHiremath
* Votes:   11

```

class Solution {//O(n^2)
    public int longestRepeatingSubstring(String S) {
        int n = S.length();
        int[][] dp = new int[n + 1][n + 1];//dp[i][j] means # of repeated chars for substrings ending at i and j
        int res = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (S.charAt(i - 1) == S.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        return res;
    }
}
```

```

class Solution {//O(n^2*logn)
	public int longestRepeatingSubstring(String s) {
		int n = s.length();
		String[] suffix = new String[n];// all strings in suffix[] has different starting position
		for (int i = 0; i < n; i++) {
			suffix[i] = s.substring(i);
		}
		Arrays.sort(suffix);//lexicographic order
		int res = 0;
		for (int i = 1; i < n; i++) {
			String a = suffix[i - 1], b = suffix[i];//!!!every adjacent pair since repeating substrings should be neighbors
			int len = Math.min(a.length(), b.length());
			for (int j = 0; j < len; j++) {
				if (a.charAt(j) != b.charAt(j)) break;
				res = Math.max(res, j + 1);
			}
		}
		return res;
    }
}
```
