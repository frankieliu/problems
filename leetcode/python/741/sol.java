
My Approach seems to be correct , getting incorrect answer

https://leetcode.com/problems/cherry-pickup/discuss/243816

* Lang:    java
* Author:  Vinoth_96
* Votes:   0

```
class Solution {
    public int cherryPickup(int[][] grid) {
        
     int N = grid.length;
        
        int[][] dp;
        char[][] track;
        
        boolean f = true;
        
        int sum = 0;
        
        while(f)
        {
            dp = new int[N][N];
            track = new char[N][N];
            
            dp[0][0] = grid[0][0];
            track[0][0] = \'a\';
            
            char c;
            
            c=\'u\';
            
            for(int i=1;i<N;i++)
            {
              if(c==\'r\'||grid[i][0]==-1)
              {
                  c=\'r\';
                  dp[i][0]=-1;
              }
                else
                    dp[i][0] = dp[i-1][0] + grid[i][0];
                
                track[i][0] = c;
            }
            
            c=\'s\';
            
            for(int j=1;j<N;j++)
            {
                if(c==\'r\'||grid[0][j]==-1)
                {
                    c=\'r\';
                    dp[0][j]=-1;
                }
                else
                    dp[0][j] = dp[0][j-1] + grid[0][j];
                
                track[0][j] = c;
            }
            
            for(int i=1;i<N;i++)
                for(int j=1;j<N;j++)
                {
                    if(grid[i][j]==-1||(track[i-1][j]==\'r\' && track[i][j-1]==\'r\'))
                    {
                        track[i][j] = \'r\';
                        dp[i][j] = -1;
                    }
                    else
                    {
                        if(dp[i-1][j]>=dp[i][j-1])
                        {
                            track[i][j] = \'u\';
                            dp[i][j] = dp[i-1][j] + grid[i][j];
                        }
                        else
                        {
                            track[i][j] = \'s\';
                            dp[i][j] = dp[i][j-1] + grid[i][j];
                        }
                    }
                }
            
            
            if(dp[N-1][N-1]<=0)
                break;
            
            System.out.println();
            for(int i=0;i<N;i++)
            {
                System.out.println();
                for(int j=0;j<N;j++)
                    System.out.print(dp[i][j] + " ");
            }
             System.out.println();
            
            sum += dp[N-1][N-1];
            
            int r = N-1 , cr = N-1;
            
            while(r>0||cr>0)
            {
                grid[r][cr]=0;
                if(track[r][cr]==\'s\')
                    cr--;
                else
                    r--;
            }
            
             System.out.println();
            for(int i=0;i<N;i++)
            {
                System.out.println();
                for(int j=0;j<N;j++)
                    System.out.print(grid[i][j] + " ");
            }
             System.out.println();
            
            grid[0][0] = 0;
        }
        
       
        return sum;
        
    }
}
```

Can someone help.
