
C++, 12 lines BFS and 7 lines DFS

https://leetcode.com/problems/employee-importance/discuss/112605

* Lang:    cpp
* Author:  zefengsong
* Votes:   6

**BFS**
```
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*>m;
        for(auto x: employees) m[x->id] = x;
        int sum = 0;
        deque<Employee*>q;
        q.push_back(m[id]);
        while(!q.empty()){
            auto p = q.front();
            q.pop_front();
            for(auto x: p->subordinates) q.push_back(m[x]);
            sum += p->importance;
        }
        return sum;
    }
};
```
***
**DFS**
```
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*>m;
        for(auto x: employees) m[x->id] = x;
        int sum = 0;
        DFS(m, id, sum);
        return sum;
    }
    
    void DFS(unordered_map<int, Employee*>& m, int id, int& sum){
        sum += m[id]->importance;
        for(auto x: m[id]->subordinates) DFS(m, x, sum);
    }
};
```
