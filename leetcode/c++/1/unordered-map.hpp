class Solution {
public:
    void printme() {
        unordered_map<string, int>
            m({{"hello", 1},
               {"goodbye", 2}});
        for (auto& x: m) {
            cout << x.first << ":" << x.second << endl;
        }
        if (m.find("hello") != m.end()) {
            cout << m["hello"] << endl;
        }
    }
};
