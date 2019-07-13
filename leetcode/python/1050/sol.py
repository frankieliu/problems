In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1050.actors-and-directors-who-cooperated-at-least-three-times.database.json

Concise Solution Using HAVING Clause

https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/discuss/297530

* Lang:    python
* Author:  zac4
* Votes:   4

```SQL
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(1) >= 3
```

