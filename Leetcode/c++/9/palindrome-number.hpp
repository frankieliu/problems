class Solution {
public:
    bool isPalindrome(int x) {
        // keep dividing by 10, store the number then do the comparisons
        vector <int> s;

        if (x<0) return false;
                     
        while (x > 0) {
            int y = x/10;
            int r = x-y*10;
            s.push_back(r);
            x=y;
        }

        int sl = s.size();
            
        for (int i = 0; i < sl/2; i++) {
            if(s[i] != s[sl-i-1]) return false;
        }
        return true;
    }
};
