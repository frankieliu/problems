In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1049.last-stone-weight-ii.algorithms.json

[Java/C++/Python] Easy Knapsacks DP

https://leetcode.com/problems/last-stone-weight-ii/discuss/294888

* Lang:    python
* Author:  lee215
* Votes:   84

Chinese explanation for contest this week on [bilibili](https://www.bilibili.com/video/av52875326).

# **Intuition**
Same problem as:
Divide all numbers into two groups,
what is the minimum difference between the sum of two groups.
Now it\'s a easy classic knapsack problem.
<br>


# **Brief Prove**
All cases of "cancellation of rocks" can be expressed by two knapsacks.
And the last stone value equals to the difference of these two knapsacks
It needs to be noticed that the opposite proposition is wrong.


# **Solution 1**
## **Explanation**:
Very classic knapsack problem solved by DP.
In this solution, I use `dp` to record the achievable sum of the smaller group.
`dp[x] = 1` means the sum `x` is possible.
<br>

## **Time Complexity**:
`O(NS)` time,
`O(S)` space, where `S = sum(A)`.
<br>

**Java, use array:**
```
    public int lastStoneWeightII(int[] A) {
        boolean[] dp = new boolean[1501];
        dp[0] = true;
        int sumA = 0, res = 100;
        for (int a : A) {
            sumA += a;
            for (int i = sumA; i >= a; --i)
                dp[i] |= dp[i - a];
        }
        for (int i = sumA / 2; i > 0; --i)
            if (dp[i]) return sumA - i - i;
        return 0;
    }
```

**C++, use bitset:**
```
    int lastStoneWeightII(vector<int> A) {
        bitset<1501> dp = {1};
        int sumA = 0, res = 100;
        for (int a : A) {
            sumA += a;
            for (int i = sumA; i >= a; --i)
                dp[i] = dp[i] + dp[i - a];
        }
        for (int i = sumA / 2; i > 0; --i)
            if (dp[i]) return sumA - i - i;
        return 0;
    }
```

**Python, use set:**
```
    def lastStoneWeightII(self, A):
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)
```
<br>




# **Solution 2**

## **Explanation**:
Adapted dp to this problem.
In this solution, I use `dp` to record the achievable diff of one group.
If `x` in the set `dp`, it means the difference `x` is achievable currently.
<br>

## **Time Complexity**:
`O(NS)` time,
`O(S)` space, where `S = sum(A)`.
<br>

**Python, use set:**
```
    def lastStoneWeightII(self, A):
        dp, sumA = {0}, sum(A)
        for a in A:
            dp = {a + x for x in dp} | {a - x for x in dp}
        return min(abs(x) for x in dp)
```
<br>




# Follow-up:
As this problem will be quite boring as Q4 (if you read my post),
I\'ll leave you a slightly harder problem as follow-up just for more fun.
Question: Return the **biggest** possible weight of this stone?
<br>




# FAQ (Some high voted questions)
**Question:** How is it a knapsack problem?
My understanding of Knapsack problem is this-
You are given a set of items , for each of which we have a weight `w[i]` and value `v[i]`.
Now we have a bag for capacity `W` and we maximize our profit.
**Answer:**
`w[i] = 1`
`v[i] = stones[i]`
`W = sum(stones) / 2`
<br>

**Question:** Why the minimum result of cancellation is equal to minimum knapsack partition?
**Answer:**
1. One cancellation can be represented as one grouping.
One grouping can be represented as one knapsack partition.
2. If the grouping difference < max(A), it can be realized by a cancellation.
With the 2 conclusions above,
we can know that the minimum result of cancellation is equal to minimum grouping difference,
which we solved by knapsack problem.
<br>

**Question:** In some version of solution, what does the magic number 1500 mean?
**Answer:**
The `dp[i]` present if the sum of one group can be `i`.
So we can only record the smaller one for less space cost,
which less than half of the upper bound of total sum 3000.

