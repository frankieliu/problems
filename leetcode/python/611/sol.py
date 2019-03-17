
Aggregate by side lengths - a different approach

https://leetcode.com/problems/valid-triangle-number/discuss/104166

* Lang:    python3
* Author:  yorkshire
* Votes:   0

Use a dictionary to count the number of sides of each length. Then let sides i, j and k be all combinations of the available side lengths.
If any of i, j and k are identical then we need to check there are enough sides to allow duplicates in the triangle, and consider the number of ways to choose those sides out of all of that length.

This is O(n^3) in the general case but performs better if there are many repeated sides.

```
    def triangleNumber(self, nums):

        sides = Counter(nums)
        if 0 in sides:
            del sides[0]
        sides = list(sides.items())  # tuples of (side length, count)
        sides.sort()
        triangles = 0

        def binom(n, k):
            if k > n:
                return 0
            return factorial(n) // (factorial(n - k) * factorial(k))

        for i, (s1, c1) in enumerate(sides):
            for j, (s2, c2) in enumerate(sides[i:]):
                j2 = j + i
                for s3, c3 in sides[j2:]:
                    if s1 == s2 == s3:  # all sides same length
                        triangles += binom(c1, 3)
                    elif s1 == s2:      # shortest 2 sides are same lenght
                        if s1 + s2 > s3:
                            triangles += c3 * binom(c1, 2)
                    elif s2 == s3:      # longest sides are same length
                        triangles += c1 * binom(c2, 2)
                    else:   # all different lengths
                        if s1 + s2 > s3:
                            triangles += c1 * c2 * c3

        return triangles
```
