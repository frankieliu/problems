
Graph walking in python - detailed explanation with video

https://leetcode.com/problems/evaluate-division/discuss/88262

* Lang:    python3
* Author:  3v3rgr33n
* Votes:   6

Hi!
This is deeply explained in [this youtube video](https://youtu.be/e2TYsOs-Sfw), but the summary is:

Given a / b = 2.0, b / c = 3.0 we can write following equations:
*   a = 2b
*   b = 3c
*   b = .5a
*   c = 1/3*b

This can be represented as a hash-of-hashes:
```
        {
            'a' : {
                'b' : 2
            },
            'b' : {
                'a' : .5,
                'c' : 3,
            },
            'c' : {
                'b' : .333333,
            }
       }
```
And the problem becomes easier, since now we can walk thru a "virtual graph", where nodes are `a, b, c`, and edges have weights `2, .5, 3, .33333`.
The path shouldn't be exactly the shortest, just any.
So we can write a recursive function which calculates the "cost" of a path `a~~~>b` by checking following 3 cases:
*  `a=b` => cost is `1` if `a` is `b`
*  `a->b` => cost is `hash[a][b]` if `a` is connected to `b` directly
*  `a->key~~~>b` => cost is `hash[a][key] * recursive_call(key, b)` if `a` is connected to `key`, which hash a path to `b`

During the implementation of this recursive function, we'd have to use `seen` set to avoid loops.

Special cases, like `a/a, x/x, a/e` (where `a` is known, but `x` and `e` are not) we can do extra checks to cut off unnecessary recursive calls.

Final solution:
```
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        self.hash = self.prepHash(equations, values)
        return [self.solve(x[0], x[1]) for x in queries]
    
    def prepHash(self, equations, values):
        hash = defaultdict(lambda: {})
        for i in xrange(len(values)):
            eq = equations[i]
            val = values[i]
            hash[eq[0]][eq[1]] = 0.0+val
            hash[eq[1]][eq[0]] = 1/(0.0+val)
        return hash
        
    def solve(self, a, b):
        res = self.rec(a, b, set([a]))
        if res is None:
            return -1.0
        return res
        
    # solves a/b
    # a ~~~~> b
    # a=b
    # a->b
    # a->key~~~>b
    def rec(self, a, b, seen):
        if a == b:
            return 1.0 if a in self.hash else None
        if a not in self.hash or b not in self.hash:
            return None
        if b in self.hash[a]: 
            return self.hash[a][b]
        else:
            for key in self.hash[a]:
                if key not in seen:
                    seen.add(key) 
                    res = self.rec(key, b, seen)
                    if res is not None:
                        return self.hash[a][key] * res
        return None
```

I hope that [the video](https://youtu.be/e2TYsOs-Sfw) was not too boring and long, but I made it to explain the whole process of solving this task as if you were coding on a whiteboard. This can be helpful for those who goes to onsite interviews soon. Anyways, please, leave comments here or below the video if you have them - I'll answer and improve! Good luck!
