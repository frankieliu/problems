
JAVA PriorityQueue Solution

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85186

* Lang:    java
* Author:  peaceTea
* Votes:   0

```java
    private class ArrayElement {
        private int[] array;
        public int ptr;
        public int min;

        public ArrayElement(int[] array) {
            this.array = array;
            this.ptr = 0;
            this.min = array[ptr];
        }

        public boolean getNextMin() {
            if (++ptr == array.length) return false;
            this.min = array[ptr];
            return true;
        }
    }

    private static class Compare implements Comparator<ArrayElement> {

        @Override
        public int compare(ArrayElement o1, ArrayElement o2) {
            return Integer.compare(o1.min, o2.min);
        }
        public static final Compare COMPARE_HEAP_ENTRIES = new Compare();
    }

    public int kthSmallest(int[][] matrix, int k) {
        Queue<ArrayElement> heap = new PriorityQueue<>(Compare.COMPARE_HEAP_ENTRIES);
        int rst = 0;
        
        for (int i = 0; i < matrix.length; i++) {
            heap.offer(new ArrayElement(matrix[i]));
        }

        for (int i = 0; i < k; i++) {
            ArrayElement tmp = heap.poll();
            rst = tmp.min;
            if (tmp.getNextMin()) heap.offer(tmp);
        }

        return rst;
    }
```
If there are n sub Arrays, Complexity will be O(log(n) + klog(n))
