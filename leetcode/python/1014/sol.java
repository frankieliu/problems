
[Java] Simple java solution with explanation

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256756

* Lang:    java
* Author:  haketakestar
* Votes:   6

Step1: Find the minimum possible weight i.e. max(largest value in the array, weight on a ship when the weight is evenly distributed)
Step2: Now use it as max limit for a ship and try to fit items.
Step3: If all the items are filled. TADA!! you have your answer. if not increament the current weight and goto Step2.

```java
class Solution {
    public int shipWithinDays(int[] weights, int D) {
        /*
         * Find the least possible capacity of ship. It will be maximum of -> the
         * largest item or the weight on one ship if the weight is evenly distributed on
         * all the ships i.e. (sum_of_all_items)/(total_ships)
         */
        int heaviestItem = weights[0];
        int weightSum = 0;
        for (int x : weights) {
            heaviestItem = Math.max(heaviestItem, x);
            weightSum += x;
        }
        int avgWeightOnShip = (int) weightSum / D;
        // Minimum required weight capacity of a ship
        int minWeight = Math.max(heaviestItem, avgWeightOnShip);

        // Start from minimum possible size to maximum possible
        for (int i = minWeight; i <= weights.length * minWeight; i++) {
            int[] ship = new int[D];
            int index = 0;
            // Fill all the ships
            for (int j = 0; j < ship.length; j++) {
                // Try to fit as many items as possible
                while (index < weights.length && ship[j] + weights[index] < i) {
                    ship[j] += weights[index];
                    index++;
                }
            }
            if (index == weights.length)
                return i - 1;
        }
        return 0;
    }
}

```

Update 1: Added `avgWeightOnShip` (thanks to @minnie101) calculation and updated variable names.
