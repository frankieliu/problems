class Solution {
public:
    int lengthOfLastWord(string s) {
        int from = s.length() - 1;
        for (int i = from; i >= 0; i--) {
            if (s[i] == ' ') {
                int ans = from - i;
                if (ans == 0 && i > 0) {
                    from = i - 1;
                    cout << from << endl;
                    continue;
                } else {
                    return ans;
                }
            }
        }
        return from + 1;
    }
};
