
Short Python O(log n) Solution

https://leetcode.com/problems/h-index-ii/discuss/71093

* Lang:    python3
* Author:  girikuncoro
* Votes:   10

The idea is to do binary search to find the min index such that `citations[i] >= len(citations) - i`, then the answer is `len(citations)-i`

    def hIndex(self, citations):
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if citations[mid] >= n-mid:
                r = mid - 1
            else:
                l = mid + 1
        return n-l
