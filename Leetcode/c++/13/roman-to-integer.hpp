class Solution {
public:
    map<char, int> m = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}};

    int romanToInt(string s) {
        char lastc = 'q';
        int ss = 0;
        for (char c : s) {
            ss += m[c];
            if (((c == 'X')||(c == 'V'))&&(lastc == 'I')) ss -= 2;
            if (((c == 'L')||(c == 'C'))&&(lastc == 'X')) ss -= 20;
            if (((c == 'D')||(c == 'M'))&&(lastc == 'C')) ss -= 200;
            lastc = c;
        }
        return ss;
    }
};
