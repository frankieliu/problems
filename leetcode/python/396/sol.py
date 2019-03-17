
O(n) solution in python - detailed explanation with video

https://leetcode.com/problems/rotate-function/discuss/87849

* Lang:    python3
* Author:  3v3rgr33n
* Votes:   2

Hi!

### VIDEO EXPLANATION

This topic is deeply explained in [the following youtube video](https://youtu.be/iIiiI2Ea67A), but you can find the summary below

### TRIVIAL, BROUTE-FORCE SOLUTION

Just calculate all of the F(k) for k in range(n) using formulas explained in examples:
```
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
...
```
This would would have a quadratic complexity O(n^2) because we'd do n multiplications for each k, and there are n values which k takes. Because of such big complexity, broute-force solution is not accepted by the judge.

### MORE OPTIMAL SOLUTION REUSING F(K-1) WHEN CALCULATING F(K)
Given that we can calculate both `sum(A)` and `F(0)` in O(n), this can be considered almost free when compared to O(n^2).
Now let's do the observation which will help us reuse `sum(A)` and `F(0)` when calculating F(k):

```
sum(A) = 4 + 3 + 2 + 6
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = ?
```
Let's re-group (1 * 4), (2 * 3), etc. in F(1):
```
F(1) = (0 * 6) +  (1 * 4)      +  (2 * 3)      +  (3 * 2)
F(1) = (0 * 6) + ((0 * 4) + 4) + ((1 * 3) + 3) + ((2 * 2) + 2)
F(1) = (0 * 6) +  (0 * 4)      +  (1 * 3)      + (2 * 2)     + 4 + 3 + 2
F(1) = (0 * 6) +  (0 * 4)      +  (1 * 3)      + (2 * 2)     + 4 + 3 + 2
F(1) = (0 * 6) +  (0 * 4)      +  (1 * 3)      + (2 * 2)     + sum(A) - 6
F(1) = (0 * 6) +  F(0) - (3 * 6)                             + sum(A) - 6
F(1) =            F(0) - (3 * 6)                             + sum(A) - 6
F(1) = F(0) + sum(A) - (1+3)*6
F(1) = F(0) + sum(A) - n*6
```
Let's apply same principle to other `k`s:
```
F(1) = F(0) + sum(A) - n*6
F(2) = F(1) + sum(A) - n*2
F(3) = F(2) + sum(A) - n*3
```
Looking at how array A changes when it rotates (`A'` is `A` rotated by 1 element, `A''` is `A` rotates by 2 elements), we can notice how last element's index can be calculated for the previous rotation. This index will be used for next rotation as part of `n*6`, `n*2`, `n*3`, etc.
```
       0  1  2  3
A   = [4, 3, 2, 6] k=0 carry_index = n-1; A[3]  =  A[n-1]        = 6
A'  = [6, 4, 3, 2] k=1 carry_index = n-2; A'[3]  = A[n-2] = A[2] = 2
A'' = [2, 6, 4, 3] k=2 carry_index = n-3; A''[3] = A[n-3] = A[1] = 3
```
So, we can write a recursive definition `F(k)=F(k-1) + sum(A) - n*A[n-k]`

SOLUTION
```
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_A = sum(A)
        n = len(A)
        prev_F = reduce(lambda acc, it: acc + A[it]*it, xrange(n), 0)
        max_F = prev_F

        for k in xrange(1, n):
            carry_index = (n-k) % n
            prev_F = prev_F + sum_A - n*A[carry_index]
            if max_F < prev_F:
                max_F = prev_F
        return max_F
```


### FINAL THOUGHTS

I hope that [the video](https://youtu.be/iIiiI2Ea67A) was not too boring and long, but I made it to explain the whole process of solving this task as if you were coding on a whiteboard. This can be helpful for those who goes to onsite interviews soon. Anyways, please, leave comments here or below the video if you have them - I'll answer and improve! Good luck!
