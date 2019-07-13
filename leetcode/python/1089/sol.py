In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1089.duplicate-zeros.algorithms.json

[C++/Java] Two Pointers, Space O(1)

https://leetcode.com/problems/duplicate-zeros/discuss/312727

* Lang:    python
* Author:  lee215
* Votes:   57

# **Intuition**
The problem can be easy solved:
1. with a copy (extra space)
2. by inserting zeros (extra time)
<br>

**Python, with extra space**
```
    def duplicateZeros(self, A):
        A[:] = [x for a in A for x in ([a] if a else [0, 0])][:len(A)]
```
<br>

# **Explanation**
We can improve it to `O(N)` time and `O(1)` space.
Basically, we apply two pointers.
`i` is the position in the original array,
`j` is the position in the new array.
(the original and the new are actually the same array.)

The first we pass forward and count the zeros.
The second we pass backward and assign the value from original input to the new array.
so that the original value won\'t be overridden too early.
<br>

**C++:**
```
    void duplicateZeros(vector<int>& A) {
        int n = A.size(), j = n + count(A.begin(), A.end(), 0);
        for (int i = n - 1; i >= 0; --i) {
            if (--j < n)
                A[j] = A[i];
            if (A[i] == 0 && --j < n)
                A[j] = 0;
        }
    }
```

**Java**
Version suggested by @davidluoyes
```java
    public void duplicateZeros(int[] arr) {
        int countZero = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) countZero++;
        }
        int len = arr.length + countZero;
        //We just need O(1) space if we scan from back
        //i point to the original array, j point to the new location
        for (int i = arr.length - 1, j = len - 1; i >= 0 && j >= 0; i--, j--) {
            if (arr[i] != 0) {
                if (j < arr.length) arr[j] = arr[i];
            } else {
                if (j < arr.length) arr[j] = arr[i];
                j--;
                if (j < arr.length) arr[j] = arr[i]; //copy twice when hit \'0\'
            }
        }
    }
```
