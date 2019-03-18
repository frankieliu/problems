
Python 1-liner

https://leetcode.com/problems/battleships-in-a-board/discuss/90990

* Lang:    python3
* Author:  dalwise
* Votes:   4

```
def countBattleships(self, b):
    return sum(all([b[y][x]=='X',x<1 or b[y][x-1]!='X',y<1 or b[y-1][x]!='X']) for y in range(len(b)) for x in range(len(b[0])))
```
Same concept in a few more lines for better readability. Count the top&left corner of each ship:

```
def countBattleships(self, board):
    res = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if all([board[y][x] == 'X',
                    not x or board[y][x-1] != 'X',
                    not y or board[y-1][x] != 'X']):
                res += 1
    return res
