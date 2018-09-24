class Solution {
public:
    int mySqrt(int x) {
        long xx = x;
        while (xx > x/xx) {
            xx = (xx + x/xx) / 2;
            cout << xx << endl;
        }
        return xx;
    }
};
