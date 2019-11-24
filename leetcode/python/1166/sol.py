In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1166.design-file-system.algorithms.json

[Java/Python 3] 7 line simple HashMap code w/ analysis.

https://leetcode.com/problems/design-file-system/discuss/365901

* Lang:    python
* Author:  rock
* Votes:   14

If `path` already exist or its parent path non-exist, return false; Otherwise, create a new path and value.

**Java**
```
    Map<String, Integer> file = new HashMap<>(); 
    
    public FileSystem() {
        file.put("", -1);
    }
    
    public boolean create(String path, int value) {
        int idx = path.lastIndexOf("/");
        String parent = path.substring(0, idx);
        if (!file.containsKey(parent)) { return false; }
        return file.putIfAbsent(path, value) == null;   
    }
    
    public int get(String path) {
        return file.getOrDefault(path, -1);
    }

```

----

**Python 3**
```
    def __init__(self):
        self.d = {"" : -1}

    def create(self, path: str, value: int) -> bool:
        parent = path[:path.rfind(\'/\')]
        if parent in self.d and path not in self.d:
            self.d[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.d.get(path, -1)
```

**Analysis:**

Time & Space:
create(): `O(path.length())`, get(): `O(1)`.
 
 space:
 file(): 
 In worst case, e.g., `path = "/a/b/c/d/e/f/g/..."`, all the path family cost `2 + 4 + 6 + ... + 2n = n * (n + 1)`. So the space cost `O(path.length() ^ 2)`.
