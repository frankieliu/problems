class Solution {
public:
    map<char,char> m={{'(',')'},
                      {'[',']'},
                      {'{','}'}};
    
    bool isValid(string s) {
        // keep a stack
        stack<char> st;
        int n = s.size();
        if (n == 0) return true;
        else {
            int i=0;
            st.push(s[i]);
            // cout << "head: " << st.top() << " i: " << i << endl;
            i++;
            while(i < n) {
                char next = s[i];
                // cout << "next: " << next << endl;
                if (st.empty() || (next != m[st.top()])) {
                    st.push(next);
                } else {
                    if (next == m[st.top()]) {
                        // cout << "next == head" << endl;
                        st.pop();
                    }
                }
                i++;
            }
            if (st.empty())
                return true;
            else
                return false;
        }
    }
};
