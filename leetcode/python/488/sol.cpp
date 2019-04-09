
488. Zuma Game - CPP - Solution

https://leetcode.com/problems/zuma-game/discuss/97040

* Lang:    cpp
* Author:  yuanhuiyang
* Votes:   0

```
// 488. Zuma Game
// https://leetcode.com/problems/zuma-game/
#include <iostream>
#include <cassert>
#include <string>
using namespace std;
class Solution {
public:
	int findMinStep(string board, string hand) {
		int result = -1;
		if (!board.empty() && hand.empty()) {
			return result;
		}
		for (size_t i = 0; i < board.size(); i++) {
			size_t j = string::npos;
			if ((j = hand.find(board[i])) != string::npos) {
				if (i + 1 < board.size() && board[i] == board[i + 1]) {
					string nextBoard = board.substr(0, i) + board.substr(i + 2);
					size_t begin = string::npos;
					while ((begin = validate(nextBoard)) != string::npos) {
						nextBoard = collapse(nextBoard, begin);
					}
					string nextHand = hand.substr(0, j) + hand.substr(j + 1);
					if (nextBoard.empty()) {
						return result = 1;
					}
					int nextResult = -1;
					if ((nextResult = findMinStep(nextBoard, nextHand)) != -1) {
						if (result == -1) {
							result = 1 + nextResult;
						}
						else {
							result = min(result, 1 + nextResult);
						}
					}
					i++;
					continue;
				}
				string nextBoard = board.substr(0, i) + hand[j] + board.substr(i);
				size_t begin = string::npos;
				while ((begin = validate(nextBoard)) != string::npos) {
					nextBoard = collapse(board, begin);
				}
				string nextHand = hand.substr(0, j) + hand.substr(j + 1);
				if (nextBoard.empty()) {
					return result = 1;
				}
				int nextResult = -1;
				if ((nextResult = findMinStep(nextBoard, nextHand)) != -1) {
					if (result == -1) {
						result = 1 + nextResult;
					}
					else {
						result = min(result, 1 + nextResult);
					}
				}
				continue;
			}
		}
		return result;
	}
private:
	size_t validate(const string& board) {
		for (size_t i = 0; i + 2 < board.size(); i++) {
			if (board.substr(i, 3) == string(3, board[i])) {
				return i;
			}
		}
		return string::npos;
	}
	string collapse(const string& board, const size_t begin) {
		size_t end = begin;
		while (end < board.size() && board[end] == board[begin]) {
			end++;
		}
		return board.substr(0, begin) + board.substr(end);
	}
};
int main(void) {
	Solution solution;
	int result = 0;
	
	result = solution.findMinStep("WRRBBW", "RB");
	assert(-1 == result);

	result = solution.findMinStep("WWRRBBWW", "WRBRW");
	assert(2 == result);

	result = solution.findMinStep("G", "GGGGG");
	assert(2 == result);

	result = solution.findMinStep("RBYYBBRRB", "YRBGB");
	assert(3 == result);

	result = solution.findMinStep("WBBWW", "WRBRW");
	assert(1 == result);

	cout << "\
Passed All\
";
	return 0;
}
```
