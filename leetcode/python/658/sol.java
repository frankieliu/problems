
Binary Search and Two Pointers  - 18 ms

https://leetcode.com/problems/find-k-closest-elements/discuss/106451

* Lang:    java
* Author:  Mr-Bin
* Votes:   6

Noticing the array is sorted, so we can using binary search to get a rough area of target numbers, and then expand it to the left k-1 more and right k-1 more elements, then searching from the left to right. If the left element is more close or equal to the target number x than the right element, then move the right index to the left one step. Otherwise, move the left index to right one step. Once, the element between the left and right is k, then return the result.

**Java**
```java
public class Solution {
	public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
		int index = Collections.binarySearch(arr, x);
		if (index == -1)
			return arr.subList(0, k);
		else if (index >= arr.size())
			return arr.subList(arr.size() - k, arr.size());
		else {
			if (index < 0)
				index = -index - 1;
			int left = Math.max(0, index - k - 1), right = Math.min(arr.size() - 1, index + k - 1);

			while (right - left > k - 1) {
				if (left < 0 || (x - arr.get(left)) <= (arr.get(right) - x))
					right--;
				else if (right > arr.size() - 1 || (x - arr.get(left)) > (arr.get(right) - x))
					left++;
				else
					System.out.println("unhandled case: " + left + " " + right);
			}

			return arr.subList(left, right + 1);
		}
	}
}
```
Here is an updated version.
```java
public class Solution {
	public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
		int n = arr.size();
		if (x <= arr.get(0)) {
			return arr.subList(0, k);
		} else if (arr.get(n - 1) <= x) {
			return arr.subList(n - k, n);
		} else {
			int index = Collections.binarySearch(arr, x);
			if (index < 0)
				index = -index - 1;
			int low = Math.max(0, index - k - 1), high = Math.min(arr.size() - 1, index + k - 1);

			while (high - low > k - 1) {
				if (low < 0 || (x - arr.get(low)) <= (arr.get(high) - x))
					high--;
				else if (high > arr.size() - 1 || (x - arr.get(low)) > (arr.get(high) - x))
					low++;
				else
					System.out.println("unhandled case: " + low + " " + high);
			}
			return arr.subList(low, high + 1);
		}
	}
}
```
