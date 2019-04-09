
Java O(n) solution using HashMap

https://leetcode.com/problems/couples-holding-hands/discuss/113377

* Lang:    java
* Author:  neverlandzzy
* Votes:   0

A straightforward solution is just search and swap, which costs O(n^2) time and O(1) space. Refer the solution from [simonzhu91](https://discuss.leetcode.com/topic/117071/sharing-java-o-n-2-brute-force-solution-with-explanation) 

We can use a HashMap to record the index of every element, so that we don't need to do extra scan during swap.  This will optimize the time complexity to O(n). But, as a trade-off, the space complexity would be O(n) as well.

The hardest part of this problem is to prove the algorithm. Refer to [votrubac 's post](https://discuss.leetcode.com/topic/117050/na\xefve-solution-accepted-with-a-proof-wrong-difficulty)

```
    public int minSwapsCouples(int[] row) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < row.length; i++) {
        	map.put(row[i], i);
        }
        
        int result = 0;
        
        for (int i = 0; i < row.length; i += 2) {
        	if (row[i] % 2 == 0) {
        		if (row[i + 1] == row[i] + 1) {
        			continue;
        		}
        		int index = map.get(row[i] + 1);
        		int tmp = row[i + 1];
        		row[i + 1] = row[index];
        		row[index] = tmp; 
        		map.put(tmp, index);
        		map.put(row[i + 1], i + 1);
        		result++;
        	} else {
        		if (row[i + 1] == row[i] - 1) {
        			continue;
        		}
        		int index = map.get(row[i] - 1);
        		int tmp = row[i + 1];
        		row[i + 1] = row[index];
        		row[index] = tmp; 
        		map.put(tmp, index);
        		map.put(row[i + 1], i + 1);
        		result++;
        	}
        }      
        return result;
    }
```
