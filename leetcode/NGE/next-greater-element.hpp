class Solution {
 public:
    // Find the next greater element
    // This works but it is O(n^2) time
    vector<int> nge0(vector<int> in) {
        vector<int> out;
        for (auto i = 0; i < in.size(); i++) {
            auto res = -1;
            for (auto j = i+1; j < in.size(); j++) {
                if (in[j] > in[i]) {
                    res = in[j];
                    break;
                }
            }
            out.push_back(res);
        }
        return out;
    }

    // Can we do better?
    // Idea: if you can't find a greater number
    // then store it in a stack, then look at the
    // next element, ..., keep storing monotone
    // decreasing elements, until you hit a an
    // element (current) that is greater, then you pop
    // elements which are less than current.
    
    vector<int> nge(vector<int> in) {
        if (in.size() == 0) return vector<int>({});
        vector<int> out(in.size(), 0);
        stack<pair<int,int>> s;
        s.push(pair<int,int>(0,in[0]));
        for (auto i = 1; i < in.size(); i++) {
            while ((!s.empty()) && (in[i] > s.top().second))  {
                out[s.top().first] = in[i];
                s.pop();
            }
            s.push(pair<int,int>(i,in[i]));
        }
        while (!s.empty()) {
            out[s.top().first] = -1;
            s.pop();
        }
        return out;
    }
};
