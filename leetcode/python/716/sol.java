
Efficient Java solution with counting occurrences of each max value

https://leetcode.com/problems/max-stack/discuss/108949

* Lang:    java
* Author:  lchenaction
* Votes:   0

We can dramatically improve on the time complexity of popping by caching the maximum stored at or below that entry. When we pop, we evict the corresponding cached value.

The time complexity is O(1). The additional space complexity is O(n). But by observing that if an element E being pushed is smaller than the maximum element already in the stack, then this E can never be the maximum, so we do not need to record it. We can just store the sequence of maximum values in a separate stack, to avoid the possibility of duplicates, we can record the number of occurrences of each maximum value, the space complexity is between O(1) and O(n), depends on how many unique max values.

Now, how to deal with popMax()? We need to backtrack to the closest matched max element and also cache the pre popped out elements, and later push them back to reflect the new max list.

```
public class MaxStack {
	private Deque<Integer> elements;
	private Deque<MaxCount> maxCounts;

	public MaxStack() {
		elements = new ArrayDeque<>();
		maxCounts = new ArrayDeque<>();
	}

	public boolean empty() {
		return elements.isEmpty();
	}

	public int top() {
		return elements.peek() == null ? 0 : elements.peek();
	}

	public int peekMax() {
		return maxCounts.peek() == null ? 0 : maxCounts.peek().max;
	}

	public int pop() {
		if (elements.isEmpty())
			throw new IllegalStateException("pop(): empty stack");
		int x = elements.pop();
		if (x == maxCounts.peek().max) {
			maxCounts.peek().count--;
			if (maxCounts.peek().count == 0)
				maxCounts.pop();
		}
		return x;
	}

	public int popMax() {
		if (elements.isEmpty())
			throw new IllegalStateException("popMax(): empty stack");
		MaxCount maxCount = maxCounts.peek();
		// backtrack to closest max and also cache front elements
		List<Integer> cachedItems = new LinkedList<>();
		while (elements.peek() != maxCount.max) {
			cachedItems.add(0, elements.pop());
		}
		elements.pop();
		maxCount.count--;
		// remove it when count down to zero
		if (maxCount.count == 0)
			maxCounts.pop();
		// push back the cached front elements
		for (Integer t : cachedItems) {
			push(t);
		}
		return maxCount.max;
	}

	public void push(int x) {
		elements.push(x);
		if (!maxCounts.isEmpty()) {
			if (maxCounts.peek().max == x)
				maxCounts.peek().count++;
			else if (maxCounts.peek().max < x)
				maxCounts.push(new MaxCount(x, 1));
		} else {
			maxCounts.push(new MaxCount(x, 1));
		}
	}

	private class MaxCount {
		int max;
		int count;

		public MaxCount(int max, int count) {
			this.max = max;
			this.count = count;
		}
	}

	public static void main(String[] args) {
		MaxStack stack = new MaxStack();
		stack.push(5);
		stack.push(1);
		stack.push(5);
		assert stack.top() == 5;
		assert stack.popMax() == 5;
		assert stack.top() == 1;
		assert stack.peekMax() == 5;
		assert stack.popMax() == 5;
		assert stack.peekMax() == 1;
		assert stack.pop() == 1;
	}
}
```
