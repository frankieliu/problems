
Reservoir Sampling Solution

https://leetcode.com/problems/linked-list-random-node/discuss/85707

* Lang:    java
* Author:  fabrizio3
* Votes:   0

```
Random r;
ListNode head;

public Solution(ListNode head) {
	this.r = new Random();
	this.head = head;
}

public int getRandom() {
	int count = 1;
	ListNode nodeVal = head;
	ListNode curr = head;
	while(curr!=null) {
		if(r.nextInt(count++)==0) nodeVal = curr;
		curr = curr.next;
	}
	return nodeVal.val;
}
```
