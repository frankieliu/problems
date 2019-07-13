In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1051.height-checker.algorithms.json

Not a well defined problem

https://leetcode.com/problems/height-checker/discuss/299265

* Lang:    python
* Author:  kris-randen
* Votes:   81

If you consider the input 
[1,2,1,2,1,1,1,2,1]

LeetCode\'s solution (at least in today\'s contest) was 4 moves for the above problem. And it\'s coming from the sort and compare solution strategy or something similar. But the minimum number of student moves for them to be in order of non-decreasing height is 3. You move each 2 to the end of the array one by one and you can sort the array in 3 student moves. I think the definition should just be how many students are out of order.
