class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int l = strs.size();
        string s = "";
        if (l==0) return s;
        if (l==1) return strs[0];
        int j = 0;
        bool same = true;
        while (same) {
            char c = strs[0][j];
            for(int i = 1; i < l; i++) {
                if ((j == strs[i].size()) || (c != strs[i][j])) {
                    same = false;
                    break;
                }
            }
            if (same) {
                s+=c;
                j++;
            }
        }
        return s;
    }
};
