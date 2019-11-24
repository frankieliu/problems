In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1146.snapshot-array.algorithms.json

[Java/Python] Binary Search

https://leetcode.com/problems/snapshot-array/discuss/350562

* Lang:    python
* Author:  lee215
* Votes:   29

## **Intuition**
Instead of copy the whole array,
we can only record the changes of `set`.
<br>

## **Explanation**
The idea is, the whole array can be large,
and we may take the `snap` tons of times.
(Like you may always ctrl + S twice)

Instead of record the history of the whole array,
we will record the history of each cell.
And this is the minimum space that we need to record all information.

For each `A[i]`, we will record its history.
With a `snap_id` and a its value.

When we want to `get` the value in history, just binary search the time point.
<br>

## **Complexity**
Time `O(logS)`
Space `O(S)`
where `S` is the number of `set` called.

`SnapshotArray(int length)` is `O(N)` time
`set(int index, int val)` is O(1) in Python and `O(logSnap)` in Java
`snap()` is `O(1)`
`get(int index, int snap_id)` is `O(logSnap)`
<br>

**Java**
```java
class SnapshotArray {
    TreeMap<Integer, Integer>[] A;
    int snap_id = 0;
    public SnapshotArray(int length) {
        A = new TreeMap[length];
        for (int i = 0; i < length; i++) {
            A[i] = new TreeMap<Integer, Integer>();
            A[i].put(0, 0);
        }
    }

    public void set(int index, int val) {
        A[index].put(snap_id, val);
    }

    public int snap() {
        return snap_id++;
    }

    public int get(int index, int snap_id) {
        return A[index].floorEntry(snap_id).getValue();
    }
}
```

**Python:**
```python
class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in xrange(n)]
        self.snap_id = 0
        self.n = n

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]
```

