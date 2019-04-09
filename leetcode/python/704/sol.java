
Java 2ms, (iterative and recursive solutions)

https://leetcode.com/problems/binary-search/discuss/259046

* Lang:    java
* Author:  kbenriquez
* Votes:   0

```
// Iterative solution
public int search(int[] nums, int target) {
	int start = 0;
	int end = nums.length-1;
	int mid = (start+end)/2;
	while(start <= end){
		if(nums[mid] == target) return mid;
		if(target < nums[mid])
			end = mid-1;
		else
			start = mid+1;
		mid = (start+end)/2;
	}

	return -1;
}

// ---------------------------------------------------

// Recursive solution
public int search(int[] nums, int target) {
	return binarySearch(nums, 0, nums.length/2, nums.length-1, target);
}
    
public int binarySearch(int[] nums, int start, int mid, int end, int target){
	if(nums[mid] == target)
		return mid;
	if(start == end)
		return -1;
	else if(target < nums[mid])
		return binarySearch(nums, start, (start+mid-1)/2, mid-1, target);
	else
		return binarySearch(nums, mid+1, (mid+1+end)/2, end, target);
}
```
