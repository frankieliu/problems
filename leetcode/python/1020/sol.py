
C++ 6 lines O(n), target sum

https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/260885

* Lang:    cpp
* Author:  votrubac
* Votes:   20

## Intuition
We can find our target sum by aggregating all numbers and dividing the result by 3.
Then we sum numbers again and track how many times we get the target sum. 
> Note that if the target sum is zero, we can reach it more than 3 times (thanks [@prateek_123](https://leetcode.com/prateek_123/) for the find!)
## Solution
```
bool canThreePartsEqualSum(vector<int>& A, int parts = 0) {
  auto total = accumulate(begin(A), end(A), 0);
  if (total % 3 != 0) return false;
  for (auto i = 0, sum = 0; i < A.size() && parts < 3; ++i) {
    sum += A[i];
    if (sum == total / 3) ++parts, sum = 0;
  }
  return parts == 3;
}
```
## Complexity Analysis
Runtime: *O(n)*. We process each element in A twice.
Memory: *O(1)*.
