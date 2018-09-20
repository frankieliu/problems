class Solution {
public:
    int strStr(string haystack, string needle) {

        if (needle.length() == 0) return 0;
        
        auto n = needle.begin();
        char b = *n;

        int i = 0;
        auto it = haystack.begin();
        auto end = haystack.end();

        for (; it != end; i++, it++) {
            if (*it == b) {
                int j = 1;
                auto ms = needle.begin(); ms++;
                bool found = true;
                for (auto me = needle.end(); ms != me; ms++, j++) {
                    if (((it + j) == end) || (*(it + j) != *ms)) {
                        found = false;
                        break;
                    }
                }
                if (found) {
                    return i;
                }
            }
        }
        return -1;
    }
};
