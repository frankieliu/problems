In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1125.smallest-sufficient-team.algorithms.json

[Python] DP Solution

https://leetcode.com/problems/smallest-sufficient-team/discuss/334572

* Lang:    python
* Author:  lee215
* Votes:   32

[Youtube](https://www.youtube.com/watch?v=Up8iyOrq-5Y)

## **Explanation**
`dp[skill_set]` is a sufficient team to cover the `skill_set`.
For each `people`,
update `his_skill` with all current combinations of `skill_set` in `dp`.


## **Complexity**
Time `O(people * 2^skill)`
Space `O(2^skill)`
<br>

**Python:**
```python
    def smallestSufficientTeam(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in dp.items():
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
```

