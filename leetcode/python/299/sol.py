
Python 3 lines solution

https://leetcode.com/problems/bulls-and-cows/discuss/74644

* Lang:    python3
* Author:  xcv58
* Votes:   42

use `Counter` to count `guess` and `secret` and sum their overlap. Then use `zip` to count `A`.

        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)
