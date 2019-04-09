
Climbing Stairs and Combination Sum 4 Similarity, Java Dynamic Programming.

https://leetcode.com/problems/combination-sum-iv/discuss/85140

* Lang:    java
* Author:  SanD91
* Votes:   0

In climbing stairs problem we have only two choices for numbers i.e. {1,2}. The same problem can be extended for any numbers, which is what combination sum4 problem is.

Climbing Stairs, solution. I know there is a easier solution, using fibonacci series. I am giving this solution because it is similar to combination sum 4 solution.

```
public class Solution {
    public static int climbStairs(int n) {
		if(n <= 0) {
			return 0;
		}

		int[] nums = new int[]{1,2};
		return combinationSum4(nums, n);
	}

	public static int combinationSum4(int[] nums, int target) {
		if(nums == null || nums.length == 0 || target < 0) {
			return 0;
		}
		//Arrays.sort(nums); //Not required, but can help in exit out of loop early.
		int[] combinations = new int[target + 1];
		combinations[0] = 1;
		int length = nums.length; // so that length is not calculated every time.
		for (int i = 1; i <= target; i++) {
			for (int j = 0; j < length; j++) {
				if(i - nums[j] < 0) {
					break;
				}
				if( i == nums[j]) {
					combinations[i] += 1;
				}
				else if (i - nums[j] >= 0) {
					combinations[i] += combinations[i - nums[j]];
				}
			}
		}
		return combinations[target];
	}
}
```

Combination Sum 4 solution

```
public static int combinationSum41(int[] nums, int target) {
	if(nums == null || nums.length == 0 || target < 0) {
		return 0;
	}
	Arrays.sort(nums); //Not required, but can help in exit out of loop early.
	int[] combinations = new int[target + 1];
	combinations[0] = 1;
	int length = nums.length; // so that length is not calculated every time.
	for (int i = 1; i <= target; i++) {
		for (int j = 0; j < length; j++) {
			if(i - nums[j] < 0) {
				break;
			}
			if( i == nums[j]) {
				combinations[i] += 1;
			}
			else if (i - nums[j] >= 0) {
				combinations[i] += combinations[i - nums[j]];
			}
		}
	}
	return combinations[target];
}
```
