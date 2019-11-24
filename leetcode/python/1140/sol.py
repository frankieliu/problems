In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1140.stone-game-ii.algorithms.json

[Java] DP with memorization, easy to understand(with explanation)

https://leetcode.com/problems/stone-game-ii/discuss/345354

* Lang:    python
* Author:  eecandy
* Votes:   27

```
class Solution {
    private int[] sums;//the sum from piles[i] to the end
    private int[][] hash;
    public int stoneGameII(int[] piles) {
        if(piles == null || piles.length == 0) return 0;
        int n = piles.length;
        sums = new int[n];
        sums[n-1] = piles[n-1];
        for(int i = n -2; i>=0;i--) {
            sums[i] = sums[i+1] + piles[i]; //the sum from piles[i] to the end
        }
        
        hash = new int[n][n];
        return helper(piles, 0, 1);
    }
    
    private int helper(int[] a, int i, int M) {
        if(i == a.length) return 0;
        if(2*M >= a.length - i) {
            return sums[i];
        }
        if(hash[i][M] != 0) return hash[i][M];
        int min = Integer.MAX_VALUE;//the min value the next player can get
        for(int x=1;x<=2*M;x++){
            min = Math.min(min, helper(a, i+x, Math.max(M,x)));
        }
        hash[i][M] = sums[i] - min;  //max stones = all the left stones - the min stones next player can get
        return hash[i][M];   
    }
}
