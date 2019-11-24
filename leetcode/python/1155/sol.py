In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1155.number-of-dice-rolls-with-target-sum.algorithms.json

C++ Coin Change 2

https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355940

* Lang:    python
* Author:  votrubac
* Votes:   46

This problem is like [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/), with the difference that the total number of coins (dices) should be equal to ```d```.
# Basic Solution (TLE)
A basic brute-force solution could be to try all combinations of all faces for all dices, and count the ones that give a total sum of ```target```.
```
int numRollsToTarget(int d, int f, int target, int res = 0) {
  if (d == 0 || target <= 0) return d == target;
  for (auto i = 1; i <= f; ++i)
    res = (res + numRollsToTarget(d - 1, f, target - i)) % 1000000007;
  return res;
}
```
> ```d == target``` is the shorthand for ``` d == 0 && target == 0```.
## Complexity Analysis
Runtime: O(f ^ d).
Memory: O(d) for the stack.
# Top-down DP
We memoise the previously computed results for dice ```i``` and and ```target```.

Since ```dp``` is initialized with zeros, we store there ```res + 1``` to check if the result has been pre-computed. This is an optimization for brevity and speed.
```
int dp[31][1001] = {};
int numRollsToTarget(int d, int f, int target, int res = 0) {
  if (d == 0 || target <= 0) return d == target;
  if (dp[d][target]) return dp[d][target] - 1;
  for (auto i = 1; i <= f; ++i)
    res = (res + numRollsToTarget(d - 1, f, target - i)) % 1000000007;
  dp[d][target] = res + 1;
  return res;
}
```
## Complexity Analysis
Runtime: O(d * f * target).
Memory: O(d * target) for the memoisation.
# Bottom-Up DP
We can define our ```dp[i][k]``` as number of ways we can get ```k``` using ```i``` dices. As an initial point, there is one way to get to ```0``` using zero dices.

Then, for each dice ```i``` and face ```j```, accumulate the number of ways we can get to ```k```. 

Note that for the bottom-up solution, we can reduce our memory complexity as we only need to store counts for the previous dice.
```
int numRollsToTarget(int d, int f, int target) {
  vector<int> dp(target + 1);
  dp[0] = 1;
  for (int i = 1; i <= d; ++i) {
    vector<int> dp1(target + 1);
    for (int j = 1; j <= f; ++j)
      for (auto k = j; k <= target; ++k)
        dp1[k] = (dp1[k] + dp[k - j]) % 1000000007;
    swap(dp, dp1);
  }
  return dp[target];
}
```
## Complexity Analysis
Runtime: O(d * f * target).
Memory: O(target) as we only store counts for the last dice.
## Further Optimizations
We can re-use the same array if we process our targets backwards. Just be sure to clear the previous target count (```dp[k]```) - this value is for the previous dice and we do not need it anymore.

> Note that we need to flip the order of processing - we iterate though targets first (```k```), and then through the faces (```j```). I left the variable names the same as for the previous solution. 

Thanks [dylan20](https://leetcode.com/dylan20/) for this memory optimization tip!

You can also see that, this way, we can stop at ```dp[target]``` when processing the last dice.
```
int numRollsToTarget(int d, int f, int target) {
  int dp[target + 1] = { 1 }, i, j, k;
  for (i = 1; i <= d; ++i)
    for (k = target; k >= (i == d ? target : 0); --k)
      for (j = k - 1, dp[k] = 0; j >= max(0, k - f); --j)
        dp[k] = (dp[k] + dp[j]) % 1000000007;
  return dp[target];
}
```
