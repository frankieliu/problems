In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1095.find-in-mountain-array.algorithms.json

[Java/C++/Python] Triple Binary Search

https://leetcode.com/problems/find-in-mountain-array/discuss/317607

* Lang:    python
* Author:  lee215
* Votes:   35

Triple Binary Search, Triple Happiness.

## **Intuition**
1. Binary find peak in the mountain.
[852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search/294082)
2. Binary find the target in strict increasing array
3. Binary find the target in strict decreasing array
<br>
Personally, (just a tip)
If I want find the index, I always use `while (left < right)`
If I may return the index during the search, I\'ll use `while (left <= right)`
<br>

## **Complexity**
Time `O(logN)` Space `O(1)`
<br>

## **Some Improvement**
1. Cache the result of `get`, in case we make the same calls.
In sacrifice of `O(logN)` space for the benefit of less calls.
2. Binary search of peak is unnecessary, just easy to write.
<br>

**C++/Java**
```
    int findInMountainArray(int target, MountainArray A) {
        int n = A.length(), l, r, m, peak = 0;
        // find index of peak
        l  = 0;
        r = n - 1;
        while (l < r) {
            m = (l + r) / 2;
            if (A.get(m) < A.get(m + 1))
                l = peak = m + 1;
            else
                r = m;
        }
        // find target in the left of peak
        l = 0;
        r = peak;
        while (l <= r) {
            m = (l + r) / 2;
            if (A.get(m) < target)
                l = m + 1;
            else if (A.get(m) > target)
                r = m - 1;
            else
                return m;
        }
        // find target in the right of peak
        l = peak;
        r = n - 1;
        while (l <= r) {
            m = (l + r) / 2;
            if (A.get(m) > target)
                l = m + 1;
            else if (A.get(m) < target)
                r = m - 1;
            else
                return m;
        }
        return -1;
    }
```

**Python:**
```
    def findInMountainArray(self, target, A):
        n = len(A)
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) / 2
            if A.get(m) < A.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) / 2
            if A.get(m) < target:
                l = m + 1
            elif A.get(m) > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) / 2
            if A.get(m) > target:
                l = m + 1
            elif A.get(m) < target:
                r = m - 1
            else:
                return m
        return -1
```

