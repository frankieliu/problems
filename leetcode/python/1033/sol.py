In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1033.moving-stones-until-consecutive.algorithms.json

C++/Java 4 lines

https://leetcode.com/problems/moving-stones-until-consecutive/discuss/282836

* Lang:    python
* Author:  votrubac
* Votes:   31

Edge case 1: all three stones are next to each other (```z - x == 2```). Return ```{0, 0}```.
Edge case 2: two stones are next to each other, or there is only one space in between. Minimum moves is ```1```.

Otherwise; minimum moves are ```2```, maximum - ```z - x - 2```.

So the position of the middle stone (```y```) only matters for the minimum moves. 
```
vector<int> numMovesStones(int a, int b, int c) {
  vector<int> s = { a, b, c };
  sort(begin(s), end(s));
  if (s[2] - s[0] == 2) return { 0, 0 };
  return { min(s[1] - s[0], s[2] - s[1]) <= 2 ? 1 : 2, s[2] - s[0] - 2 };
}
```
Java version:
```
public int[] numMovesStones(int a, int b, int c) {
  int[] s = { a, b, c };
  Arrays.sort(s);
  if (s[2] - s[0] == 2) return new int[] { 0, 0 };
  return new int[] { Math.min(s[1] - s[0], s[2] - s[1]) <= 2 ? 1 : 2, s[2] - s[0] - 2 };
}
```
