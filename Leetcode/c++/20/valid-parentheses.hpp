class Solution {
public:
    map<char,char> m={{'(',')'},
                      {'[',']'},
                      {'{','}'}};
                    
    bool isValid(string s) {
        int head = 0;
        int tail = s.size()-1;
        // search head
        if (s[head] == '(')||(s[head] == '[')||(s[head] == '{') {
            while (tail > head) {
                if (s[tail] == s[head])
                    break;
                tail--;
            }
            if (tail == head) return false;
        }
    }
};
