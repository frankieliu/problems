class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        string c = "";
        int carry = 0;
        while (i >=0 && j >=0) {
            int temp = (a[i] == '1' ? 1:0) + (b[j] == '1' ? 1:0) + carry;
            carry = temp >= 2 ? 1:0;
            c = to_string(temp % 2) + c;
            cout << c << endl;
            i--; j--;
        }
        while (i >= 0) {
            int temp = (a[i] == '1' ? 1:0) + carry;
            carry = temp >= 2 ? 1:0;
            c = to_string(temp % 2) + c;
            cout << c << endl;
            i--;
        }
        while (j >= 0) {
            int temp = (b[j] == '1' ? 1:0) + carry;
            carry = temp >= 2 ? 1:0;
            c = to_string(temp % 2) + c;
            cout << c << endl;
            j--;
        }
        if (carry == 1) {
            c = "1" + c;
        }
        return c;
    }
};
