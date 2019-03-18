
python O(n) space dp solution

https://leetcode.com/problems/coin-change-2/discuss/99210

* Lang:    python3
* Author:  yzj1212
* Votes:   26

```
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]
```
