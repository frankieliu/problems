
483. Smallest Good Base - CPP - Solution

https://leetcode.com/problems/smallest-good-base/discuss/96600

* Lang:    cpp
* Author:  yuanhuiyang
* Votes:   1

```
// 483. Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/
#include <iostream>
#include <cmath>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <limits>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;

// BEGIN: https://discuss.leetcode.com/topic/76368/python-solution-with-detailed-mathematical-explanation-and-derivation
class Solution {
public:
	string smallestGoodBase(string n) {
		if (n == "0") {
			return "0";
		}
		if (n == "1") {
			return "1";
		}
		size_t y = stoull(n);
		for (size_t i = 1 + ceil((long double)(log(y)) / (long double)(log(2))); i > 1; i--) {
			size_t j = floor(pow((long double)(y), 1.0 / (i - 1)));
			if (j > 1) {
				size_t x = round((pow((long double)j, (long double)i) - 1) / (long double)(j - 1));
				if (x == y) {
					return to_string(j);
				}
			}
		}
		return to_string(y - 1);
	}
};
// END: https://discuss.leetcode.com/topic/76368/python-solution-with-detailed-mathematical-explanation-and-derivation

// BEGIN: Time Limit Exceeded
// class Solution {
// public:
// 	string smallestGoodBase(string n) {
// 		const size_t val = stoull(n);
// 		for (size_t k = 2; k < val; k++) {
// 			if (validate(k, val)) {
// 				return to_string(k);
// 			}
// 		}
// 		return "";
// 	}
// private:
// 	bool validate(const size_t k, size_t val) {
// 		while (val > 1) {
// 			if ((val % k) != 1) {
// 				return false;
// 			}
// 			val /= k;
// 		}
// 		return val == 1;
// 	}
// };
// END: Time Limit Exceeded

int main(void) {
	Solution solution;
	string n;
	string result;
	string answer;

	n = "470988884881403701";
	answer = "686286299";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "16035713712910627";
	answer = "502";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "14919921443713777";
	answer = "496";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "2251799813685247";
	answer = "2";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "3";
	answer = "2";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "15";
	answer = "2";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "13";
	answer = "3";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "4681";
	answer = "8";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	n = "1000000000000000000";
	answer = "999999999999999999";
	result = solution.smallestGoodBase(n);
	assert(answer == result);

	cout << "\
Passed All\
";
	return 0;
}
```
