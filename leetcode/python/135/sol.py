
Python two pass solution (left to right, then right to left).

https://leetcode.com/problems/candy/discuss/42881

* Lang:    python3
* Author:  caikehe
* Votes:   4

        
    def candy(self, ratings):
        res = len(ratings) * [1]
        for i in xrange(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in xrange(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)
