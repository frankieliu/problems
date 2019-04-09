
Java Solution, expanded from All Permutation

https://leetcode.com/problems/beautiful-arrangement/discuss/99739

* Lang:    java
* Author:  dandanbiu
* Votes:   0

```
    public int countArrangement(int N) {
        int[] counter = new int[] {0};
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            array[i] = i + 1;
        }
        helper(0, N, array, counter);
        return counter[0];
    }
    
    private void helper(int level, int n, int[] array, int[] counter) {
        if (level == n) {
            counter[0]++;
        }
        for (int i = level; i < n; i++) {
            if (array[i] % (level + 1) == 0 || (level + 1) % array[i] == 0) {
                swap(array, i, level);
                helper(level + 1, n, array, counter);
                swap(array, i, level);
            }
        }
    }
    
    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
```
