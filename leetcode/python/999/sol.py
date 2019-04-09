
Simple AC Python Solution (16 ms) Beats 100%

https://leetcode.com/problems/available-captures-for-rook/discuss/243345

* Lang:    python3
* Author:  _voyageur
* Votes:   1

Uncomment the commented lines for clarity / understanding testcases

```

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def findWhiteRook(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == \'R\':
                        return (i,j)
            return -1
        rr, rc = findWhiteRook(board)
        kills = 0
        # print("White Rook at ", rr, rc)
		
		# west
        for ic in range(rc-1,-1,-1):
            if board[rr][ic] == \'p\':
                # print("Can kill pawn at {},{}".format(rr,ic))
                kills += 1
                break
            elif board[rr][ic] == \'B\' or board[rr][ic] == \'P\':
                break
        
		# east
        for ic in range(rc+1,len(board[0])):
            if board[rr][ic] == \'p\':
                # print("Can kill pawn at {},{}".format(rr,ic))
                kills += 1
                break
            elif board[rr][ic] == \'B\' or board[rr][ic] == \'P\':
                break
        
		# south
        for ir in range(rr+1,len(board)):
            if board[ir][rc] == \'p\':
                # print("Can kill pawn at {},{}".format(ir,rc))
                kills += 1
                break
            elif board[ir][rc] == \'B\' or board[ir][rc] == \'P\':
                break
        
        # north
        for ir in range(rr-1,-1,-1):
            if board[ir][rc] == \'p\':
                # print("Can kill pawn at {},{}".format(ir,rc))
                kills += 1
                break
            elif board[ir][rc] == \'B\' or board[ir][rc] == \'P\':
                break
        return kills
                
        
```
