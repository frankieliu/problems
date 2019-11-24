In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1157.online-majority-element-in-subarray.algorithms.json

[C++] Codes of different approaches (Random Pick, Trade-off, Segment Tree, Bucket)

https://leetcode.com/problems/online-majority-element-in-subarray/discuss/356227

* Lang:    python
* Author:  zerotrac2
* Votes:   55

Some basic knowledge to understand the following methods and codes:

1. For a given interval `[l, r]` and `threshold`, we would like to find the majority which occurs at least `threshold` times. The problem also gives an inequality `2 * threshold > right - left + 1`, which means the majority must occur more than half. We denote the majority which satisfies the inequality as "more than half" majority.

2. For the "more than half" majority, the following theorem always holds: if we split the interval `[l, r]` into consecutive sub-intervals `[l, a_1], [a_1+1, a_2], ..., [a_{n-1}+1, a_n], [a_n+1, r]`, the "more than half" majority of interval `[l, r]` (if it exists) should be also the "more than half" majority of at least one sub-interval. This can be proved by contradiction.

3. By the theorem in 2, we can split the interval `[l, r]` into sub-intervals and find the "more than half" majority of each sub-interval and check whether it is the "more than half" majority of the interval `[l, r]`.

4. We can use [Boyer\u2013Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) to find the "more than half" majority in `O(n)` time.

5. We can use a `unordered_map<int, vector<int>>` to store the positions of each number in `[l, r]`. The key in the `unordered_map` represents a number and the value represents the positions of that number in increasing order. Thus we can count the occurrences of a number in a given interval `[l, r]` in `O(log(n))` time by using binary search (in C++ we can use `lower_bound` and `upper_bound` to simplify the code).

6. We can combine 4 and 5 together to check whether the "more than half" majority occurs at least `threshold` times. The time complexity is the same as 4, since `O(n + log(n)) = O(n)` holds.

I will show 4 different method with brief explanations below. I will use the sign `No.x` to reference the basic knowledge with number `x`. `No.6` is often used to find the "more than half" majority in a short sub-interval, while `No.5` is often used to find the "more than half" majority in a long interval after finishing the sub-interval calculations, as `No.3` states.

Random Pick:
As the majority occurs more than half in the interval `[l, r]`, we will have the probability of more than `1/2` to find the "more than half" majority if we randomly pick a number in the interval. Thus, if we randomly pick `try_bound` times, we will have the probability of `(1-(1/2)) ** try_bound` not to find the "more than half" majority. The probability will be less than `1e-6` if we set `try_bound` as `20`. If we find nothing in `try_bound` times, we can claim that there is no "more than half" majority.
Here we use `No.5` to count the occurrences of a randomly picked number.

Runtime: ~200 ms
Pre-calculation: `O(n)`
Query: `O(try_bound * log(n))`

```
class MajorityChecker {
private:
    unordered_map<int, vector<int>> pos;
    vector<int> a;
    int try_bound;
    
public:
    MajorityChecker(vector<int>& arr): a(arr) {
        srand(time(nullptr));
        for (int i = 0; i < arr.size(); ++i) {
            pos[arr[i]].push_back(i);
        }
        try_bound = 20;
    }
    
    int get_occurrence(int num, int l, int r) {
        auto iter = pos.find(num);
        if (iter == pos.end()) {
            return 0;
        }
        const auto& vec = iter->second;
        auto iter_l = lower_bound(vec.begin(), vec.end(), l);
        if (iter_l == vec.end()) {
            return 0;
        }
        auto iter_r = upper_bound(vec.begin(), vec.end(), r);
        return iter_r - iter_l;
    }
    
    int get_random(int l, int r) {
        return rand() % (r - l + 1) + l;
    }
    
    int query(int left, int right, int threshold) {
        for (int i = 0; i < try_bound; ++i) {
            int elem = a[get_random(left, right)];
            if (get_occurrence(elem, left, right) >= threshold) {
                return elem;
            }
        }
        return -1;
    }
};
```

Trade-off:
This method is based on the fact that number of "popular" numbers (i.e. a number which occurs at least `t` times) cannot exceed `n/t`. Thus, if the `threshold` in a given query is not less than `t`, there is only `n/t` candidate "more than half" majorities.
We can design an algorithm to handle different queries with different methods. For the queries with `threshold` less than `t`, the length of interval `[l, r]` will also smaller than `2t`, so we can simply use `No.6` to find the "more than half" majority in `O(t)` time. For the queries with `threshold` more than `t`, we iterate through the "popular" numbers and use `No.5` to check whether it is a "more than half" majority in `[l, r]`. This is solved in `O((n/t) * log(n/t))` time, `O(n/t)` for the iteration and `O(log(n/t))` for `No.5`. Thus, the total time complexity is the maximum of `O(t)` and `O((n/t) * log(n/t))`. We can do a trade-off by solving the equation `t = (n/t) * log(n/t)`, but it is too difficult. However, we can simply set `t` as `sqrt(n)` to get a pretty good trade-off, and the time complexity will be `O(sqrt(n) * log(n))`.

Runtime: ~200 ms
Pre-calculation: `O(n)`
Query: `O(sqrt(n) * log(n))`

```
class MajorityChecker {
private:
    unordered_map<int, vector<int>> pos;
    unordered_set<int> popular;
    vector<int> a;
    int lookup_bound;
    
public:
    MajorityChecker(vector<int>& arr): a(arr) {
        for (int i = 0; i < arr.size(); ++i) {
            pos[arr[i]].push_back(i);
        }
        lookup_bound = round(sqrt(arr.size()));
        for (const auto& [key, value]: pos) {
            if (value.size() >= lookup_bound) {
                popular.insert(key);
            }
        }
    }
    
    int vote(int l, int r) {
        int target = a[l], occ = 1;
        for (int i = l + 1; i <= r; ++i) {
            if (a[i] == target) {
                ++occ;
            }
            else {
                --occ;
                if (occ < 0) {
                    target = a[i];
                    occ = 1;
                }
            }
        }
        int cnt = 0;
        for (int i = l; i <= r; ++i) {
            if (a[i] == target) {
                ++cnt;
            }
        }
        if (cnt * 2 > r - l + 1) {
            return target;
        }
        return -1;
    }
    
    int get_occurrence(int num, int l, int r) {
        auto iter = pos.find(num);
        if (iter == pos.end()) {
            return 0;
        }
        const auto& vec = iter->second;
        auto iter_l = lower_bound(vec.begin(), vec.end(), l);
        if (iter_l == vec.end()) {
            return 0;
        }
        auto iter_r = upper_bound(vec.begin(), vec.end(), r);
        return iter_r - iter_l;
    }
    
    int query(int left, int right, int threshold) {
        if (threshold <= lookup_bound) {
            int candidate = vote(left, right);
            if (candidate != -1 && get_occurrence(candidate, left, right) >= threshold) {
                return candidate;
            }
            return -1;
        }
        else {
            for (const int& elem: popular) {
                if (get_occurrence(elem, left, right) >= threshold) {
                    return elem;
                }
            }
            return -1;
        }
    }
};
```

Segment tree:
Segment tree is a perfect data structure for this problem because it can divide an interval into consecutive sub-intervals. The nodes in the segment tree store the "more than half" majority (if it exists) or `-1` of the corresponding interval `[l, r]`. We use `No.5` to merge the interval `[l, mid]` and `[mid + 1, r]` in the "build tree" process.
During the query process, we can search the interval `[l, r]` on the segment tree and get `O(log(n))` sub-intervals. For each sub-interval, we use `No.5` to check if it is the "more than half" majority of `[l, r]`, which is another `O(log(n))` time.

Runtime: ~200ms
Pre-calculation: `O(n * log(n))`
Query: `O(log(n) * log(n))`

```
class MajorityChecker {
private:
    unordered_map<int, vector<int>> pos;
    vector<int> tree;
    vector<int> a;
    
public:
    MajorityChecker(vector<int>& arr): a(arr) {
        for (int i = 0; i < arr.size(); ++i) {
            pos[arr[i]].push_back(i);
        }
        tree = vector<int>(arr.size() * 4, -1);
        build_tree(1, 0, arr.size() - 1);
    }
    
    void build_tree(int tree_pos, int l, int r) {
        if (l == r) {
            tree[tree_pos] = a[l];
            return;
        }
        int mid = (l + r) >> 1;
        build_tree(tree_pos * 2, l, mid);
        build_tree(tree_pos * 2 + 1, mid + 1, r);
        if (tree[tree_pos * 2] != -1 && get_occurrence(tree[tree_pos * 2], l, r) * 2 > r - l + 1) {
            tree[tree_pos] = tree[tree_pos * 2];
        }
        else if (tree[tree_pos * 2 + 1] != -1 && get_occurrence(tree[tree_pos * 2 + 1], l, r) * 2 > r - l + 1) {
            tree[tree_pos] = tree[tree_pos * 2 + 1];
        }
    }
    
    pair<int, int> query(int tree_pos, int l, int r, int queryl, int queryr) {
        if (l > queryr || r < queryl) {
            return make_pair(-1, -1);
        }
        if (queryl <= l && r <= queryr) {
            if (tree[tree_pos] == -1) {
                return make_pair(-1, -1);
            }
            int occ = get_occurrence(tree[tree_pos], queryl, queryr);
            if (occ * 2 > queryr - queryl + 1) {
                return make_pair(tree[tree_pos], occ);
            }
            else {
                return make_pair(-1, -1);
            }
        }
        int mid = (l + r) >> 1;
        pair<int, int> res_l = query(tree_pos * 2, l, mid, queryl, queryr);
        if (res_l.first > -1) {
            return res_l;
        }
        pair<int, int> res_r = query(tree_pos * 2 + 1, mid + 1, r, queryl, queryr);
        if (res_r.first > -1) {
            return res_r;
        }
        return make_pair(-1, -1);
    }
    
    int get_occurrence(int num, int l, int r) {
        auto iter = pos.find(num);
        if (iter == pos.end()) {
            return 0;
        }
        const auto& vec = iter->second;
        auto iter_l = lower_bound(vec.begin(), vec.end(), l);
        if (iter_l == vec.end()) {
            return 0;
        }
        auto iter_r = upper_bound(vec.begin(), vec.end(), r);
        return iter_r - iter_l;
    }
    
    int query(int left, int right, int threshold) {
        pair<int, int> ans = query(1, 0, a.size() - 1, left, right);
        if (ans.second >= threshold) {
            return ans.first;
        }
        return -1;
    }
};
```

Bucket:
The bucket method also focus on splitting `[l, r]` into sub-intervals. We break the interval into `t` buckets with size `n/t`. We pre-calculate the "more than half" majority of each bucket by `No.6`. For a given query `[l, r]`, we find the bucket id `b_l` and `b_r` which contains `l` and `r`. If `b_l` equals to `b_r`, it means the whole interval lies in one bucket, we can use `No.6` to find the "more than half" majority in `O(t)` time. If `b_l` is not equal to `b_r`, we can divide the interval into `[l, r_border(b_l)], b_{l+1}, ..., b_{r-1}, [l_border(b_r), r]`, where `l_border` and `r_border` represent the left and right border of a bucket. We find the "more than half" majority of complete buckets by the pre-calculation and the first & last sub-interval by `No.6`. We get no more than `n/t` candidates now and we check each by `No.5` to find the "more than half" majority. The time complexity is `O(t + (n/t) * log(t))`, which is more than the previous `O(t)`. Thus we come to the trade-off to minimize `O(t + (n/t) * log(t))`. We can set `t` as `sqrt(n)` to get a pretty good trade-off `O(sqrt(n) * log(n))`.

Runtime: ~400ms
Pre-calculation: `O(n)`
Query: `O(sqrt(n) * log(n))`

```
class MajorityChecker {
private:
    unordered_map<int, vector<int>> pos;
    vector<int> a;
    vector<int> bucket;
    int bucket_size;
    
    
public:
    MajorityChecker(vector<int>& arr): a(arr) {
        for (int i = 0; i < arr.size(); ++i) {
            pos[arr[i]].push_back(i);
        }
        bucket_size = round(sqrt(a.size()));
        int l = 0;
        while (l < a.size()) {
            int r = min(l + bucket_size, (int)a.size()) - 1;
            bucket.push_back(vote(l, r));
            l += bucket_size;
        }
    }
    
    int vote(int l, int r) {
        int target = a[l], occ = 1;
        for (int i = l + 1; i <= r; ++i) {
            if (a[i] == target) {
                ++occ;
            }
            else {
                --occ;
                if (occ < 0) {
                    target = a[i];
                    occ = 1;
                }
            }
        }
        int cnt = 0;
        for (int i = l; i <= r; ++i) {
            if (a[i] == target) {
                ++cnt;
            }
        }
        if (cnt * 2 > r - l + 1) {
            return target;
        }
        return -1;
    }
    
    int get_occurrence(int num, int l, int r) {
        auto iter = pos.find(num);
        if (iter == pos.end()) {
            return 0;
        }
        const auto& vec = iter->second;
        auto iter_l = lower_bound(vec.begin(), vec.end(), l);
        if (iter_l == vec.end()) {
            return 0;
        }
        auto iter_r = upper_bound(vec.begin(), vec.end(), r);
        return iter_r - iter_l;
    }
    
    int query(int left, int right, int threshold) {
        int bucket_l = left / bucket_size;
        int bucket_r = right / bucket_size;
        if (bucket_l == bucket_r) {
            int candidate = vote(left, right);
            if (candidate != -1 && get_occurrence(candidate, left, right) >= threshold) {
                return candidate;
            }
            return -1;
        }
        else {
            int vote_l = vote(left, (bucket_l + 1) * bucket_size - 1);
            int vote_r = vote(bucket_r * bucket_size, right);
            if (vote_l != -1 && get_occurrence(vote_l, left, right) >= threshold) {
                return vote_l;
            }
            if (vote_r != -1 && get_occurrence(vote_r, left, right) >= threshold) {
                return vote_r;
            }
            for (int i = bucket_l + 1; i < bucket_r; ++i) {
                int occ = get_occurrence(bucket[i], left, right);
                if (occ >= threshold) {
                    return bucket[i];
                }
            }
            return -1;
        }
    }
};
```

