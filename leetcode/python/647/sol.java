
Share 3 methods, DP method and extend method, Java

https://leetcode.com/problems/palindromic-substrings/discuss/105714

* Lang:    java
* Author:  MadDetective
* Votes:   3

```
// ------------- DP method 1: O(N^3)------------------
public class Solution {
    public int countSubstrings(String s) {
        if(s==null || s.isEmpty()) return 0;
        final int N = s.length();
        int[][] dp = new int[N][N];
        for(int i=0; i<N; i++){
            dp[i][i] = 1;
        }
        for(int i=N-2; i>=0; i--){
            for(int j=i+1; j<N; j++){
                int self = isPalindrom(s, i, j) ? 1 : 0;
                dp[i][j] = self + dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1];
            }
        }
        return dp[0][N-1];
    }
    
    private boolean isPalindrom(String s, int left, int right){
        while(left<right){
            if(s.charAt(left)!=s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
}

// ------------- DP method 2: O(N^2) (about N^2/2) ------------------
public class Solution {
    public int countSubstrings(String s) {
        if(s==null || s.isEmpty()) return 0;
        final int N = s.length();
        boolean[][] dp = new boolean[N][N];
        for(int i=0; i<N; i++){
            dp[i][i] = true;
        }
        int count = N;
        for(int i=N-2; i>=0; i--){
            for(int j=i+1; j<N; j++){
                if(s.charAt(i)==s.charAt(j) && (j-i<=2 || dp[i+1][j-1])){
                    dp[i][j] = true;
                    count ++;
                }
            }
        }
        return count;
    }
}

// ------------- extend method: O(N^2) (about N^2/4)------------------
public class Solution {
    public int countSubstrings(String s) {
        if(s==null || s.isEmpty()) return 0;
        int count = 0;
        for(int i=0; i<s.length(); i++){
            count += extendPalindrom(s, i, i) + extendPalindrom(s, i, i+1);
        }
        return count;
    }
    
    private int extendPalindrom(String s, int left, int right){
        int count = 0;
        while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
            count++;
            left--;
            right++;
        }
        return count;
    }
}

```
