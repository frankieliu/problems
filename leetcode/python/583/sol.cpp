
C++ 6 lines DP

https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103221

* Lang:    cpp
* Author:  zefengsong
* Votes:   0

C++ version of this [post](https://discuss.leetcode.com/topic/89285/java-dp-solution-longest-common-subsequence).

`dp[i][j]`: The longest common subsequence at `word1[i - 1]` and `word2[j - 1]`.
```
int minDistance(string word1, string word2) {
    // dp[i][j] = word1[i - 1] == word2[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
    vector<vector<int>>dp(word1.size() + 1, vector<int>(word2.size() + 1));
    for(int i = 0; i <= word1.size(); i++)
        for(int j = 0; j <= word2.size(); j++)
            dp[i][j] = !i || !j ? 0 : word1[i - 1] == word2[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
    int LCS = dp[word1.size()][word2.size()];
    return (word1.size() - LCS) + (word2.size() - LCS);
}
```
