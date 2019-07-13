In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1063.number-of-valid-subarrays.algorithms.json

C++ O(n) stack

https://leetcode.com/problems/number-of-valid-subarrays/discuss/314317

* Lang:    python
* Author:  votrubac
* Votes:   2

# Intuition
If element ```i``` is the smallest one we encountered so far, it does not form any valid subarrays with any of the previous elements. Otherwise, it form a valid subarray starting from each previous element that is smaller.

For this example ```[2, 4, 6, 8, 5, 3, 1]```:
- ```8```: forms 4 valid subarrays (starting from 2, 4, 6, and 8)
- ```5``` forms 3 valid subarrays (2, 4, and 5)
- ```3``` forms 2 valid subarrays (2 and 3)
- ```1``` forms 1 valid subarray (1)
# Solution
Maintain monotonically increased values in a stack. The size of the stack is the number of valid subarrays between the first and last element in the stack.
```
int validSubarrays(vector<int>& nums, int res = 0) {
  vector<int> s;
  for (auto n : nums) {
    while (!s.empty() && n < s.back()) s.pop_back();
    s.push_back(n);
    res += s.size();
  }
  return res;
}
```
# Complexity Analysis
Runtime: *O(n)*. We process each element no more than twice.
Memory: *O(n)*.
