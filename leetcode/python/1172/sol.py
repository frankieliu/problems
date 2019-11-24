In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1172.dinner-plate-stacks.algorithms.json

[C++/Python] Two Solutions

https://leetcode.com/problems/dinner-plate-stacks/discuss/366331

* Lang:    python
* Author:  lee215
* Votes:   19

## Solution 1
Use a list `stacks` to save all stacks.
Use a heap queue `q` to find the leftmost available stack.

push, `O(logN)` time
pop, amortized `O(1)` time
popAtStack, `O(logN)` time

**Python**
```python
    def __init__(self, capacity):
        self.c = capacity
        self.q = []
        self.stacks = []

    def push(self, val):
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q)
        if not self.q:
            heapq.heappush(self.q, len(self.stacks))
        if self.q[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index)
            return self.stacks[index].pop()
        return -1
```


## Solution 2
Use a map `m` to keep the mapping between index and stack
Use a set `available` to keep indices of all no full stacks.


**C++:**
```cpp
    int c;
    map<int, vector<int>> m;
    set<int> available;

    DinnerPlates(int capacity) {
        c = capacity;
    }

    void push(int val) {
        if (available.empty())
            available.insert(m.size());
        m[*available.begin()].push_back(val);
        if (m[*available.begin()].size() == c)
            available.erase(available.begin());
    }

    int pop() {
        if (m.empty()) return -1;
        return popAtStack(m.rbegin()->first);
    }

    int popAtStack(int index) {
        if (!m.count(index) || m[index].empty())
            return -1;
        int val = m[index].back();
        m[index].pop_back();
        available.insert(index);
        if (m[index].empty())
            m.erase(index);
        return val;
    }
```

