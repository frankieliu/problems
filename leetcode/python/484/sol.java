
Greedy O(n) JAVA solution with explanation

https://leetcode.com/problems/find-permutation/discuss/96663

* Lang:    java
* Author:  dettier
* Votes:   22

Idea is pretty simple. There are 2 possibilities:
1. String starts with `"I"`. Then we should use 1 as the first item.
2. String starts with `"D..DI"` (`k` letters) or the string is just `"D...D"`. In this case we should use `k, k - 1, ..., 1` to get lexicographically smallest permutation.

Then we proceed computing the rest of the array. Also we should increase `min` variable that is used to store minimum value in remaining part of the array.

```
public int[] findPermutation(String s) {
    
    s = s + ".";
    int[] res = new int[s.length()];
    int min = 1, i = 0;

    while (i < res.length) {
        if (s.charAt(i) != 'D') {
            res[i++] = min++;
        } else {
            int j = i;
            while (s.charAt(j) == 'D') j++;
            for (int k = j; k >= i; k--)
                res[k] = min++;
            i = j + 1;
        }
    }

    return res;
}
```
