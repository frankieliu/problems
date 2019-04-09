
Java Fisher-Yates Shuffle & In-Place Swap

https://leetcode.com/problems/shuffle-an-array/discuss/86007

* Lang:    java
* Author:  fabrizio3
* Votes:   1

```
private int[] nums;
private Random r;

public Solution(int[] nums) {
	this.nums = nums;
	r = new Random();
}

public int[] reset() {
	return this.nums;
}

public int[] shuffle() {
	int[] shuffledNums = Arrays.copyOf(nums,nums.length);
	for(int i=1; i<shuffledNums.length; i++) {
		swap(shuffledNums,i,r.nextInt(i+1));
	}
	return shuffledNums;
}

public void swap(int[] nums, int i, int j) {
	if(nums[i]==nums[j]) return;
	nums[i] = nums[i]^nums[j];
	nums[j] = nums[i]^nums[j];
	nums[i] = nums[i]^nums[j];
}
```
