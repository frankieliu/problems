
[Java] Simple 9 line one pass O(n) in O(1) space with explanation

https://leetcode.com/problems/largest-number-at-least-twice-of-others/discuss/112891

* Lang:    java
* Author:  mfcndw
* Votes:   0

Apparently the problem can be described as: Is the largest element in the array equal or bigger than twice of the second largest one.

Each new element i we meet will falls into these three range:
1. (max, 99] - we need to update previous second to max, then max to i;
2. (second, max) - only need to update second to i;
3. [0, second) - nothing need to be changed

And don't remember we need the max index. So have extra variable to track that.

Of course you can use max and second to directly track the index element, but as I tried there's some edge case that make me think simply save the value will be easier. For example case [1] or [1, 0].

```
public int dominantIndex(int[] nums) {
        int max = 0, second = 0, maxIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (max < nums[i]) {
                second = max;
                max = nums[i];
                maxIndex = i;
            } else if (second < nums[i]) second = nums[i];
        }
        return max >= 2 * second ? maxIndex : -1;
    }
