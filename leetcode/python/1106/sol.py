In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1106.parsing-a-boolean-expression.algorithms.json

[Python] Easy 1-line Cheat

https://leetcode.com/problems/parsing-a-boolean-expression/discuss/323307

* Lang:    python
* Author:  lee215
* Votes:   27

## **Intuition**
Well, we can see that `&`, `|` and `!` are just three functions.
And in python, they are function `all`, `any` and keyword `not`.

## **Explanation**
Following the description,
it demands us to evaluate the expression.
So no recursion and no stack, I just `eval` the expression.
<br>

## **Complexity**
Time `O(N)`
Sapce `O(N)`
I guess it\'s not fast compared with string parse, but wow it\'s `O(N)`.
<br>

**Python:**
```
    def parseBoolExpr(self, S, t=True, f=False):
        return eval(S.replace(\'!\', \'not |\').replace(\'&(\', \'all([\').replace(\'|(\', \'any([\').replace(\')\', \'])\'))
```
