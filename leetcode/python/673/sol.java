
Another O(N ^ 2) around 35ms Java DP solution derived from LIS problem

https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/107330

* Lang:    java
* Author:  haruhiku
* Votes:   0

```
class Solution {
    public int findNumberOfLIS(int[] nums) {
        if (nums == null || nums.length < 1) {
            return 0;
        }
        int n = nums.length;
        int len = 0;
        List<Integer>[] dp = new List[n];
        int[] count = new int[n];
        for (int i = 0; i < n; ++i) {
            int left = 0;
            int right = len;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (nums[i] > nums[dp[mid].get(dp[mid].size()-1)]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if (left == len) {
                ++len;
            }
            if (dp[left] == null) {
                dp[left] = new ArrayList<>();
            }
            dp[left].add(i);
            if (left == 0) {
                count[i] = 1;
            } else {
                for (int index : dp[left-1]) {
                    if (nums[index] < nums[i]) {
                        count[i] += count[index];
                    } 
                }
            }
        }
        int sum = 0;
        for (int index : dp[len-1]) {
            sum += count[index];
        }
        return sum;
    }
}
```
If there is a way to simply this part to O(logN), then I think there should be a solution of O(NlogN) in total.
```
            if (left == 0) {
                count[i] = 1;
            } else {
                for (int index : dp[left-1]) {
                    if (nums[index] < nums[i]) {
                        count[i] += count[index];
                    } 
                }
            }
```
