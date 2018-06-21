class Solution {
public:
    int strStr(string haystack, string needle) {
    }

    // First find the lps (length of the longest suffix that is a prefix)
    int* lps(string needle) {
        int l = needle.length();
        int* a = new int[l];
        char h = needle[0];
        needle[0] = 0;
        for(int i = 1; i < needle.length(); i++) {
            needle[i] = 
        }
    }
    
    
};
