
0ms c++ O(n) Math and DP solutions and 47ms python solution

https://leetcode.com/problems/integer-break/discuss/80918

* Lang:    python3
* Author:  sxycwzwzq
* Votes:   3

When n is larger than 2, we need use as many factor 3 as possible to make the product larger. 
But we don't allow number 1 exists in factors. 

c++ Math: Time Complexity : O( n ); Space Complexity : O(1)

    class Solution {
    public:
        int integerBreak(int n) {
            if(n == 2) return 1;
            if(n == 3) return 2;
            
            int res = 1;
            while(n > 2){
                res *= 3;
                n -= 3;
            }
            if(n == 0) return res;
            if(n == 1) return (res / 3 ) * 4;
            if(n == 2) return res * 2;
        }
    };

c++ DP: Time Complexity : O( n ); Space Complexity : O(n)

    class Solution {
    public:
        //dp[i] means max result we can get when n = i;
        int integerBreak(int n) {
            if(n == 2) return 1;
            if(n == 3) return 2;
            vector<int> dp(n+1, 0);
            dp[2] = 2;
            dp[3] = 3;
            for(int i = 4; i <= n; i++){
                dp[i] = max(dp[i-2] * 2, dp[i-3] * 3);
            }
            return dp[n];
        }
    };


python:

    class Solution(object):
        def integerBreak(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 2:
                return 1
            if n == 3:
                return 2
            t = n % 3
            if t == 0:
                return int(math.pow(3,n/3))
            if t == 1:
                return int(math.pow(3,(n-4)/3) * 4)
            if t == 2:
                return int(math.pow(3,(n-2)/3) * 2)
