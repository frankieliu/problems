
simple count zero solution, python & c++

https://leetcode.com/problems/can-place-flowers/discuss/103969

* Lang:    python3
* Author:  zqfan
* Votes:   3

python
```
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        zero = 1  # initial has no left limit
        for slot in flowerbed:
            if slot == 0:
                zero += 1
            else:
                n -= (zero - 1) / 2 if zero else 0
                zero = 0
        n -= zero / 2  # last has no right limit
        return n <= 0
```
c++
```
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int zero = 1;
        for ( int slot : flowerbed ) {
            if ( 0 == slot ) {
                ++zero;
            } else {
                n -= zero ? (zero - 1) / 2 : 0;  // use (zero - 1) / 2 if you know -1/2 = 0 in c++
                zero = 0;
            }
        }
        n -= zero / 2;
        return n <= 0;
    }
};
```
