
C++ O(KN^2) Time, O(N) Space, Clean And Short DP

https://leetcode.com/problems/maximum-vacation-days/discuss/102669

* Lang:    cpp
* Author:  fentoyal
* Votes:   0

```
struct Solution {
    int maxVacationDays(const vector<vector<int>>& flights, const vector<vector<int>>& days)
    {
        int city_cnt = days.size();
        if (city_cnt == 0) return 0;
        int week_cnt = days.front().size();
        vector<vector<int>> dp(2, vector<int>(city_cnt, INT_MIN));
        dp[0][0] = 0;
        for (int i = 1; i <= week_cnt; ++ i)
            for (int j = 0; j < city_cnt; ++ j)
                for (int k = 0; k < city_cnt; ++ k)
                    if (flights[k][j] != 0 || k == j)
                        dp[i%2][j] = max(dp[i%2][j], dp[(i+1)%2][k] + days[j][i - 1]);
        return *max_element(dp[week_cnt % 2].begin(), dp[week_cnt % 2].end());
    }
};
```
