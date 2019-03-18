
3 lines O(n) Python with explanation/proof

https://leetcode.com/problems/wiggle-subsequence/discuss/84921

* Lang:    python3
* Author:  StefanPochmann
* Votes:   31

    def wiggleMaxLength(self, nums):
        nan = float('nan')
        diffs = [a-b for a, b in zip([nan] + nums, nums + [nan]) if a-b]
        return sum(not d*e >= 0 for d, e in zip(diffs, diffs[1:]))

**Explanation / Proof:**

Imagine the given array contains [..., **10, 10, 10, 10**, ...]. Obviously we can't use more than one of those tens, as that wouldn't be wiggly. So right away we can ignore all consecutive duplicates.

Imagine the given array contains [..., 10, **7, 11, 13, 17, 19, 23**, 20, ...]. So  increasing from 7 to 23. What can we do with that? Well we can't use more than two of those increasing numbers, as that wouldn't be wiggly. And if we do use two, we'd better use the 7 and the 23, as that offers the best extensibility (for example, the 19 wouldn't allow to next pick the 20 for the wiggly subsequence). And if we do use only one, it still should be either the 7 or the 23, as the 7 is the best wiggle-low and the 23 is the best wiggle-high of them. So whether we actually use the 7 and the 23 or not, we definitely can and should remove the 11, 13, 17, and 19. So then we have [..., 10, **7, 23**, 20, ...]. Now, notice that the 7 is a local minimum (both the 10 and the 23 are larger) and the 23 is a local maximum. And if we do this  with **all** increasing or decreasing streaks, i.e., keep only their first and last number, then all the numbers we have left are local extrema, either smaller than both neighbors or larger than both neighbors. Which means that at that point, we're already fully wiggly. And we only removed as many numbers as we have to. So it's a longest possible wiggly subsequence.

My solution first computes differences of neighbors and throws out zeros (which does get rid of those useless consecutive duplicates). And then it just counts the local extrema (by checking two consecutive differences).

I use `nan` for some convenience, I'll let you figure that part out :-)
<br>
**Alternative implementations** not using the `nan` trick: First remove repetitions, then count the local extrema except the ends, and add the number of ends (because the ends are always local extrema)

    def wiggleMaxLength(self, nums):
        norep = [num for num, _ in itertools.groupby(nums)]
        triples = zip(norep, norep[1:], norep[2:])
        return sum((b>a) == (b>c) for a, b, c in triples) + len(norep[:2])

    def wiggleMaxLength(self, nums):
        norep = [num for num, _ in itertools.groupby(nums)]
        if len(norep) < 2: return len(norep)
        triples = zip(norep, norep[1:], norep[2:])
        return 2 + sum(a<b>c or a>b<c for a, b, c in triples)
