class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> out(digits);
        int carry = 1;
        for(int i = out.size()-1; i>=0; i--) {
            out[i] = (out[i] + carry) % 10;
            if (out[i] == 0) {
                carry = 1;
            } else {
                carry = 0;
                break;
            }
        }
        if (carry == 1) {
            out.insert(out.begin(), 1, 1);
        }
        return out;
    }
};
