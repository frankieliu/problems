
Python Straight-Forward DFS

https://leetcode.com/problems/minesweeper/discuss/247365

* Lang:    python3
* Author:  joinyoung
* Votes:   0

```
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        nb = [item for row in board[max(x - 1, 0): x + 2] for item in row[max(y - 1, 0): y + 2]]
        if board[x][y] == \'M\': board[x][y] = \'X\'
        elif nb.count(\'M\'): board[x][y] = str(nb.count(\'M\'))
        else: 
            board[x][y] = \'B\'
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == \'E\':
                        _ = self.updateBoard(board, [i, j])
        return board
```
