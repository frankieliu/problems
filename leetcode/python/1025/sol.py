In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1025.divisor-game.algorithms.json

just return N % 2 == 0 (proof)

https://leetcode.com/problems/divisor-game/discuss/274566

* Lang:    python
* Author:  bupt_wc
* Votes:   100

prove it by two steps:
1. if Alice will lose for N, then Alice will must win for N+1, since Alice can first just make N decrease 1.
2. for any odd number N, it only has odd factor, so after the first move, it will be an even number

let\'s check the inference
fisrt N = 1, Alice lose. then Alice will must win for 2.
if N = 3, since all even number(2) smaller than 3 will leads Alice win, so Alice will lose for 3
3 lose -> 4 win
all even number(2,4) smaller than 5 will leads Alice win, so Alice will lose for 5
...

Therefore, Alice will always win for even number, lose for odd number.

