"""36. Valid Sudoku
Medium

667

225

Favorite

Share

Determine if a 9x9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.

Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are
filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left
    corner being modified to 8. Since there are two 8's in the top
    left 3x3 sub-box, it is invalid.

Note:

A Sudoku board (partially filled) could be valid but is not
necessarily solvable.

Only the filled cells need to be validated according to the mentioned rules.

The given board contain only digits 1-9 and the character '.'.

The given board size is always 9x9.

Accepted
202.1K
Submissions
492.9K

"""
class Solution:
    def isValidSudoku(self, b):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        col = []
        rc = []
        for i in range(0, 9):
            row.append({})
            col.append({})
            rc.append([])
            for j in range(0, 3):
                rc[i].append({})

        for i in range(0, 9):
            for j in range(0, 9):
                el = b[i][j]
                if el != '.':
                    if el in row[i]:
                        print('row', i, el, row[i])
                        return False
                    else:
                        # print("row inserting", i, el)
                        row[i][el] = 1

                    if el in col[j]:
                        print('col', i, el, col[j])
                        return False
                    else:
                        # print("col inserting", j, el)
                        col[j][el] = 1

                    if el in rc[i // 3][j // 3]:
                        print('rc', i, el, rc[i // 3][j // 3])
                        return False
                    else:
                        # print("rc inserting", i/3, j/3, el)
                        rc[i // 3][j // 3][el] = 1
        return True


s = Solution()
print(s.isValidSudoku(
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]))
print(s.isValidSudoku(
    [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
]))

print(s.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]))
