
Python O(nlogn) O(n) solution, beats 97%, with explanation

https://leetcode.com/problems/russian-doll-envelopes/discuss/82761

* Lang:    python3
* Author:  agave
* Votes:   19

    class Solution(object):
        def maxEnvelopes(self, envs):
            def liss(envs):
                def lmip(envs, tails, k):
                    b, e = 0, len(tails) - 1
                    while b <= e:
                        m = (b + e) >> 1
                        if envs[tails[m]][1] >= k[1]:
                            e = m - 1
                        else:
                            b = m + 1
                    return b
                
                tails = []
                for i, env in enumerate(envs):
                    idx = lmip(envs, tails, env)
                    if idx >= len(tails):
                        tails.append(i)
                    else:
                        tails[idx] = i
                return len(tails)
            
            
            def f(x, y):
                return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1
                
            envs.sort(cmp=f)
            return liss(envs)

    # Runtime: 100ms

The idea is to order the envelopes and then calculate the longest increasing subsequence (LISS). We first sort the envelopes by width, and we also make sure that when the width is the same, the envelope with greater height comes first. Why? This makes sure that when we calculate the LISS, we don't have a case such as [3, 4] [3, 5] (we could increase the LISS but this would be wrong as the width is the same. It can't happen when [3, 5] comes first in the ordering).

We could calculate the LISS using the standard DP algorithm (quadratic runtime), but we can just use the tails array method with a twist: we store the index of the tail, and we do leftmost insertion point as usual to find the right index in `nlogn` time. Why not rightmost? Think about the case [1, 1], [1, 1], [1, 1].
