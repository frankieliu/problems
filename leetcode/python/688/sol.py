
Python with explanations

https://leetcode.com/problems/knight-probability-in-chessboard/discuss/108197

* Lang:    python3
* Author:  flamesofmoon
* Votes:   0

In my code, I am computing the survival rate for all grids on the board after `K` steps. The rates are updated step by step. For each step, `probs[i][j]` should be the sum of the rates in the possible eight grids divided by 8.

Note that here I wrote a lengthy list comprehension in the for loop. This is not to show off. If I didn't do so, I will have to create a new 2D list, store values temporarily, and deepcopy that back to `probs` which is too much work.

```
probs = [[(1 if i<N and j<N else 0) for j in xrange(N+2)] for i in xrange(N+2)]
for t in xrange(K):
    probs = [[ (0.125 * 
               sum(probs[i+a*m1][j+(3-a)*m2] for a in [1,2] for m1 in [-1,1] for m2 in [-1,1]) 
               if i<N and j<N else 0) 
               for j in xrange(N+2)] for i in xrange(N+2)]
return probs[r][c]
```
Another interesting idea given by @StefanPochmann is [here](https://discuss.leetcode.com/topic/105635/python), in which he only computes for `probs[r][c]`, but in the way that the probability distribution of the knight at each step is computed.

I am curious if there is a mathematical solution to this problem using martingales or random walk. If you see one, please don't hesitate to @ me.
