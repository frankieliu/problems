
C++ Simple 4 Line Solution O(n)

https://leetcode.com/problems/rabbits-in-forest/discuss/114705

* Lang:    cpp
* Author:  code_report
* Votes:   0

Explanation:


1. Store count of bunnies saying n others like them in map
list item
2. We know that there must be ceil (# of bunnies saying x / x+1) groups. For example if there are 5 bunnies saying there is 1 other bunny with their color, there at minimum is 3 groups of 2 bunnies with the same color (3 = ceil (5/2))
3. So for each x, sum the num of groups * x

```
    int numRabbits(vector<int>& a) {
        unordered_map<int,double> m;
        for (int i = 0; i < a.size (); i++) m[a[i]+1]++;
        int res = 0;
        for (auto e : m) res += ceil (e.second/e.first) * e.first;
        return res;
    }
