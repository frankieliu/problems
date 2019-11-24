In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1138.alphabet-board-path.algorithms.json

C++/Java O(n)

https://leetcode.com/problems/alphabet-board-path/discuss/345278

* Lang:    python
* Author:  votrubac
* Votes:   30

Determine the coordinate and move there. Note that \'z\' is tricky as you cannot move left or right in the last row.

To account for that, make sure we move up before moving right, and move left before moving down.
## C++
```
string alphabetBoardPath(string target, int x = 0, int y = 0) {
  string res;
  for (auto ch : target) {
    int x1 = (ch - \'a\') % 5, y1 = (ch - \'a\') / 5;
    res += string(max(0, y - y1), \'U\') + string(max(0, x1 - x), \'R\') +
      string(max(0, x - x1), \'L\') + string(max(0, y1 - y), \'D\') + "!";
    x = x1, y = y1;
  }
  return res;
}
```
## Java
> Would be nice to have Java 11 support, so we can just do ```"U".repeat(Math.max(0, y - y1));```
```
public String alphabetBoardPath(String target) {
  int x = 0, y = 0;
  StringBuilder sb = new StringBuilder();
  for (char ch : target.toCharArray()) {
    int x1 = (ch - \'a\') % 5, y1 = (ch - \'a\') / 5;
    sb.append(String.join("", Collections.nCopies(Math.max(0, y - y1), "U")) +
      String.join("", Collections.nCopies(Math.max(0, x1 - x), "R")) +
      String.join("", Collections.nCopies(Math.max(0, x - x1), "L")) +
      String.join("", Collections.nCopies(Math.max(0, y1 - y), "D")) + "!");
    x = x1; y = y1;
  }
  return sb.toString();
}
```
