
Fastest Java Solution with no global variables and limited space.

https://leetcode.com/problems/path-sum-iv/discuss/106898

* Lang:    java
* Author:  SanD91
* Votes:   0

The logic is to represent the tree as a map.
So let's suppose the numbers are: [111, 217, 221, 315, 415]. The map will represent this as:
11 -> 1
21 -> 7
22 -> 1
31 -> 5
41 -> 5

After this we traverse the array again from the last element to see if it has any child nodes. If yes then it is not a leaf, move on to next. If it has no child nodes, start storing the node value while traversing above to the root node.

Let me know if you need more explanation :)

```
class Solution {
    public int pathSum(int[] nums) {
	if(nums == null || nums.length == 0 || nums[0] == 0) return 0;
	Map<Integer, Integer> path = new HashMap<>();

	for(int n: nums) {
	    path.put(n / 10, n % 10);
	}

	int curValue = 0;
	int nextLeft = 0;
	int nextRight = 0;
	int sum = 0;

	for(int i = nums.length - 1; i >= 0; --i) {
	    curValue = nums[i];
	    nextRight = (curValue / 100 + 1) * 10 + ((curValue / 10) % 10) * 2;
	    nextLeft = nextRight - 1;

	    if(!path.containsKey(nextRight) && !path.containsKey(nextLeft)) {
		curValue /= 10;
		while(curValue >= 11) {
		    sum += path.get(curValue);
		    curValue = (curValue / 10 - 1) * 10 + ((curValue % 10) - 1) / 2 + 1;
		}
            }
        }
        return sum;
    }
}
```
