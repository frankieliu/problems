In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1024.video-stitching.algorithms.json

[Java/C++/Python] Greedy Solution, O(1) Space

https://leetcode.com/problems/video-stitching/discuss/270036

* Lang:    python
* Author:  lee215
* Votes:   53

## Solution 1: Sort

Time `O(NlogN)`, Space `O(1)`
**Java**
```
    public int videoStitching(int[][] clips, int T) {
        int res = 0;
        Arrays.sort(clips, (a,b) ->  a[0] - b[0]);
        for (int i = 0, st = 0, end = 0; st < T; st = end, ++res) {
            for (; i < clips.length && clips[i][0] <= st; ++i)
                end = Math.max(end, clips[i][1]);
            if (st == end) return -1;
        }
        return res;
    }
```

**C++**
```
    int videoStitching(vector<vector<int>>& clips, int T) {
        sort(begin(clips), end(clips));
        int res = 0;
        for (auto i = 0, st = 0, end = 0; st < T; st = end, ++res) {
            for (; i < clips.size() && clips[i][0] <= st; ++i)
                end = max(end, clips[i][1]);
            if (st == end) return -1;
        }
        return res;
    }
```

**Python:**
```
    def videoStitching(self, clips, T):
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= T else -1
```

<br>

## Solution 2: Sort + DP
Sort clips first.
Then for each clip, update `dp[clip[0]] ~ dp[clip[1]]`.

Time `O(NlogN + NT)`, Space `O(T)`

**C++**
```
    int videoStitching(vector<vector<int>>& clips, int T) {
        sort(clips.begin(), clips.end());
        vector<int> dp(101, 101);
        dp[0] = 0;
        for (auto& c : clips)
            for (int i = c[0] + 1; i <= c[1]; i++)
                dp[i] = min(dp[i], dp[c[0]] + 1);
        return dp[T] >= 100 ? -1 : dp[T];
    }
```

<br>

## Solution 3: DP

Loop on i form `0` to `T`,
loop on all `clips`,
If `clip[0] <= i  <= clip[1]`, we update `dp[i]`

Time `O(NT)`, Space `O(T)`

**Java**
```
    public int videoStitching(int[][] clips, int T) {
        int[] dp = new int[T + 1];
        Arrays.fill(dp, T + 1);
        dp[0] = 0;
        for (int i = 0; i <= T && dp[i - 1] < T; i++) {
            for (int[] c : clips) {
                if (c[0] <= i && i <= c[1])
                    dp[i] = Math.min(dp[i], dp[c[0]] + 1);
            }
        }
        return dp[T] == T + 1 ? T + 1 : dp[T];
    }
```
