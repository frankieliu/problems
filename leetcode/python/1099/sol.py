In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1099.two-sum-less-than-k.algorithms.json

[Java] Sort then push from two ends.

https://leetcode.com/problems/two-sum-less-than-k/discuss/322931

* Lang:    python
* Author:  rock
* Votes:   9

# Note: 1) I have no premium subscription and can NO longer read comments under locked problems, though I can still edit my post now. 2) Sorry that I can NOT answer your questions.
---

1. Sort the input `A`;
2. Push from the two ends and attempt to find any addition of the two elements < K; if the addition >= K, then decrease the high bound and hence tentatively get a smaller addition; otherwise, increase low bound to find a bigger addition;
3. repeat 2 till the end.

```
    public int twoSumLessThanK(int[] A, int K) {
        Arrays.sort(A); // Time cost O(nlogn).
        int max = -1, i = 0, j = A.length - 1; 
        while (i < j) {
            int sum = A[i] + A[j];
            if (sum < K) { // find one candidate.
                max = Math.max(max, sum);
                ++i; // increase the smaller element.
            }else { // >= sum.
                --j; // decrease the bigger element.
            }
        }
        return max;
    }
```	

**Analysis:**

Time: O(nlogn), space: O(1), where n = A.length.
