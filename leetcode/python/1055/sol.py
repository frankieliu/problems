In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1055.shortest-way-to-form-string.algorithms.json

Python O(M + N*logM) using inverted index + binary search (Similar to LC 792)

https://leetcode.com/problems/shortest-way-to-form-string/discuss/304662

* Lang:    python
* Author:  Twohu
* Votes:   15

This is a google phone screen question. It\'s the same idea as [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/description/). I recommend solving that question first.

The idea is to create an [inverted index](https://en.wikipedia.org/wiki/Inverted_index) that saves the offsets of where each character occurs in `source`. The index data structure is represented as a hashmap, where the Key is the character, and the Value is the (sorted) list of offsets where this character appears. To run the algorithm, for each character in `target`, use the index to get the list of possible offsets for this character. Then search this list for next offset which appears after the offset of the previous character. We can use binary search to efficiently search for the next offset in our index.

Example with `source` = "abcab", `target` = "aabbaac"
The inverted index data structure for this example would be:
inverted_index  = {
a: [0, 3]   # \'a\' appears at index 0, 3 in source
b: [1, 4],  # \'b\' appears at index 1, 4 in source
c: [2],      # \'c\' appears at index 2 in source
}
Initialize `i` = -1 (i represents the smallest valid next offset) and `loop_cnt` = 1 (number of passes through source). 
Iterate through the target string "aabbaac"
a => get the offsets of character \'a\' which is [0, 3]. Set `i` to 1.
a => get the offsets of character \'a\' which is [0, 3]. Set `i` to 4.
b => get the offsets of character \'b\' which is [1, 4]. Set `i` to 5.
b => get the offsets of character \'b\' which is [1, 4]. Increment `loop_cnt` to 2, and Set `i` to 2.
a => get the offsets of character \'a\' which is [0, 3]. Set `i` to 4.
a => get the offsets of character \'a\' which is [0, 3]. Increment `loop_cnt` to 3, and Set `i` to 1.
c => get the offsets of character \'c\' which is [2]. Set `i` to 3.
We\'re done iterating through target so return the number of loops (3).

The runtime is O(M) to build the index, and O(logM) for each query. There are N queries, so the total runtime is O(M + N\\*logM). M is the length of source and N is the length of target. The space complexity is O(M), which is the space needed to store the index.

```
:::python
def shortestWay(self, source: str, target: str) -> int:
    inverted_index = collections.defaultdict(list)
    for i, ch in enumerate(source):
        inverted_index[ch].append(i)

    loop_cnt = 1
    i = -1
    for ch in target:
        if ch not in inverted_index:
            return -1
        offset_list_for_ch = inverted_index[ch]
        # bisect_left(A, x) returns the smallest index j s.t. A[j] >= x. If no such index j exists, it returns len(A).
        j = bisect.bisect_left(offset_list_for_ch, i)
        if j == len(offset_list_for_ch):
            loop_cnt += 1
            i = offset_list_for_ch[0] + 1
        else:
            i = offset_list_for_ch[j] + 1

    return loop_cnt
```

Closing thoughts: As usual, there are multiple solutions to this problem. One way other way to solve is  the naive O(M\\*N) solution using two pointers. This solution won\'t be enough to pass a phone screen. There is also a dynamic programming O(|\u03A3|\\*M + N) solution (where |\u03A3| is the size of the alphabet, or 26 in this question). xiangmo posted an [example solution here](https://leetcode.com/problems/shortest-way-to-form-string/discuss/309632/Java-O(M-+-N)-solution), which I encourage you to check out.
