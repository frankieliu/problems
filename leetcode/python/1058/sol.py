In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1058.minimize-rounding-error-to-meet-target.algorithms.json

O(n) Greedy + Selection algorithm (Java)

https://leetcode.com/problems/minimize-rounding-error-to-meet-target/discuss/303863

* Lang:    python
* Author:  mud2man
* Votes:   4

We have two choice: floor or ceil for each number. So the maximum sum we can get from prices is the sum of ceil of all prices. On the other hand, the minimum sum is the sum of floo of all prices. If the target value is not in `{min, max}`, then we return -1.  

If the `target` is in `{min, max}`, the only way we reach `target` from `prices` is that we pick `(max - target) = lowerRoundCount` number from `prices` rounded floor

So the key point here is how to get the minimum rounded error as long as we pick `lowerRoundCount` numbers with rounded floor. The answer is that we pick numbers with `lowerRoundCount` smallest rounded (to floor) error, at the same time, the non-picked number have the `(n - lowerRoundCount)` smallest rounded (to ceil) error. Because two parts (picked number with rounded floor and non-picked numbers with rounded ceil) have the minimum rounded error, the sum of two parts is minimum. 

Instead of using sort to get the `lowerRoundCount` smallest rounded errors, we can use selection alogorithm to do partition and reduce the time complexity from O(nlogn) to O(n). So the time complexity of this answer is O(n)

Steps:
1. Get `errors`(rounded to floor), `min` and `max`
2. Check if `target` is in `{min, max}`
3. Use selection algorithm `selectKthSmallest` to get the k-th smallest error, and rearrange k smallest `error`  in the first half of `errors`
4. Get the minimum rounded error  

```
import java.math.*;
class Solution {
    private BigDecimal selectKthSmallest(List<BigDecimal> errors, int lb, int hb, int k){
        if(k < lb || k > hb){
            return null;
        }
        BigDecimal pilot = errors.get(hb);
        int smallEqualIdx = lb - 1;
        for(int i = lb; i < hb; ++i){
            BigDecimal curr = errors.get(i);
            if(curr.compareTo(pilot) <= 0){
                BigDecimal tmp = errors.get(smallEqualIdx + 1);
                errors.set(++smallEqualIdx, curr);
                errors.set(i, tmp);
            }
        }
        BigDecimal tmp = errors.get(smallEqualIdx + 1);
        errors.set(++smallEqualIdx, pilot);
        errors.set(hb, tmp);
        if(smallEqualIdx == k){
            return pilot;
        }else if(smallEqualIdx > k){
            return selectKthSmallest(errors, lb, smallEqualIdx - 1, k);
        }else{
            return selectKthSmallest(errors, smallEqualIdx + 1, hb, k);
        }
    }
    
    public String minimizeError(String[] prices, int target) {
        List<BigDecimal> errors = new ArrayList<>();
        double min = 0;
        double max = 0;
        for(int i = 0; i < prices.length; ++i){
            BigDecimal price = new BigDecimal(prices[i]);
            BigDecimal floor = new BigDecimal(Math.floor(Double.valueOf(prices[i])));
            BigDecimal ceil = new BigDecimal(Math.ceil(Double.valueOf(prices[i])));
            min += Math.floor(Double.valueOf(prices[i]));
            max += Math.ceil(Double.valueOf(prices[i]));
            if(!floor.equals(ceil)){
                errors.add(price.subtract(floor));
            }
        }

        if((double)target < min || (double)target > max){
            return "-1";
        }
        int lowerRoundCount = (int)max - target;
        selectKthSmallest(errors, 0, errors.size() - 1, lowerRoundCount - 1);
        BigDecimal minError = new BigDecimal("0.000");
        for(int i = 0; i < errors.size(); ++i){
            if(i < lowerRoundCount){
                minError = minError.add(errors.get(i));
            }else{
                minError = minError.add(new BigDecimal("1.000").subtract(errors.get(i)));
            }
        }
        return minError.toString();
    }
}
```
