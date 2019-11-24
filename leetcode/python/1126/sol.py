In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1126.active-businesses.database.json

Simple Oracle Solution

https://leetcode.com/problems/active-businesses/discuss/338673

* Lang:    python
* Author:  Bang25
* Votes:   1

/* Write your PL/SQL query statement below */


with subq as
(
select event_type, avg(occurences) as average
    from events
    group by event_type)

select events.business_id as business_id
from events join subq on events.event_type = subq.event_type
and events.occurences > subq.average
group by events.business_id having count(events.business_id)>1;;
