In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1085.sum-of-digits-in-the-minimum-number.algorithms.json

C++ 5lines

https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/discuss/313073

* Lang:    python
* Author:  BarOrz
* Votes:   1

```
class Solution {
public:
    int sumOfDigits(vector<int>& A) {
        int min_node = *min_element(A.begin(),A.end());
        while(min_node > 10){
            min_node += (min_node%10)*10;
            min_node/=10;
        }
        return min_node%2==0;
    }
};
```
