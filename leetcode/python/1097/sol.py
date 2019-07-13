In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1097.game-play-analysis-v.database.json

Intuitive MySQL answer

https://leetcode.com/problems/game-play-analysis-v/discuss/320988

* Lang:    python
* Author:  tschijnmo
* Votes:   3

```
SELECT install_dt, COUNT(player_id) AS installs,
ROUND(COUNT(next_day) / COUNT(player_id), 2) AS Day1_retention
FROM (
    SELECT a1.player_id, a1.install_dt, a2.event_date AS next_day
    FROM
    (
        SELECT player_id, MIN(event_date) AS install_dt 
        FROM Activity
        GROUP BY player_id
    ) AS a1 
    LEFT JOIN Activity AS a2
    ON a1.player_id = a2.player_id
    AND a2.event_date = a1.install_dt + 1
) AS t
GROUP BY install_dt;
```
