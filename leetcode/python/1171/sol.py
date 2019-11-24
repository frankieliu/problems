In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1171.remove-zero-sum-consecutive-nodes-from-linked-list.algorithms.json

[Java/C++/Python] Greedily Skip with HashMap

https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319

* Lang:    python
* Author:  lee215
* Votes:   54

## **Update 2019-08-25**
The OJ standard solution is **WRONG**.
It won\'t block the right submit.
But wrong submit can also get accepted.

Following the test case given by @kay_deep:
`[1, 3, 2, -3, -2, 5, 100, -100, 1]`
The expected result should be `[1,5,1]` or `[1,3,2,1]`.
<br>

## **Intuition**
Assume the input is an array.
Do you know how to solve it?
Scan from the left, and calculate the prefix sum.
Whenever meet the seen prefix,
remove all elements of the subarray between them.
<br>

## **Explanation**
Because the head ListNode can be removed in the end,
I create a `dummy` ListNode and set it as a previous node of `head`.
`prefix` calculates the prefix sum from the first node to the current `cur` node.

Next step, we need an important hashmap `m` (no good name for it),
It takes a prefix sum as key, and the related node as the value.

Then we scan the linked list, accumulate the node\'s value as `prefix` sum.
1. If it\'s a prefix that we\'ve never seen, we set `m[prefix] = cur`.
2. If we have seen this prefix, `m[prefix]` is the node we achieve this prefix sum.
We want to skip all nodes between `m[prefix]` and `cur.next` (exclusive).
So we simplely do `m[prefix].next = cur.next`.

We keep doing these and it\'s done.
<br>

## **Complexity**
Time `O(N)`, one pass
Space `O(N)` for hashmap
<br>

**Java:**
```java
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0), cur = dummy;
        dummy.next = head;
        int prefix = 0;
        Map<Integer, ListNode> m = new HashMap<>();
        while (cur != null) {
            prefix += cur.val;
            if (m.containsKey(prefix)) {
                cur =  m.get(prefix).next;
                int p = prefix + cur.val;
                while (p != prefix) {
                    m.remove(p);
                    cur = cur.next;
                    p += cur.val;
                }
                m.get(prefix).next = cur.next;
            } else {
                m.put(prefix, cur);
            }
            cur = cur.next;
        }
        return dummy.next;
    }
```

**C++:**
```cpp
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode dummy(0), *cur = &dummy;
        dummy.next = head;
        int prefix = 0;
        unordered_map<int, ListNode*> m;
        while (cur) {
            prefix += cur->val;
            if (m.count(prefix)) {
                cur =  m[prefix]->next;
                int p = prefix + cur->val;
                while (p != prefix) {
                    m.erase(p);
                    cur = cur->next;
                    p += cur->val;
                }
                m[prefix]->next = cur->next;
            } else {
                m[prefix] = cur;
            }
            cur = cur->next;
        }
        return dummy.next;
    }
```

**Python:**
```python
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
```
