/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    vector<string> split(string s) {
        vector<string> vs;
        stringstream ss(s);
        string line;
        while(getline(ss, line)) {
            stringstream ls(line);
            string item;
            while(getline(ls, item, ',')) {
                vs.push_back(item);
            }
        }
        return vs;
    }

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string out;
        if (root == NULL) {
            out += "null";
        } else {
            out += to_string(root->val);
            out += ",";
            out += serialize(root->left);
            out += ",";
            out += serialize(root->right);
        }
            
        return out;
    }

    TreeNode* deserialize(queue<string> &q) {
        string ns = "null";
        if (q.empty()) {
            return NULL;
        } else {
            string s = q.front(); q.pop();
            // cout << "reading: " << s << endl;
            if (s == ns) {
                return NULL;
            } else {
                int i = stoi(s);
                TreeNode* t = new TreeNode(i);
                t->left = deserialize(q);
                t->right = deserialize(q);
                return t;
            }
        }
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue<string> q;
        for (auto x : split(data)) {
            q.push(x);
        }
        if (false) {
            queue<string> q2(q);
            for (auto x = 0; x < q2.size(); x++){
                cout << q2.front(); q2.pop();
                if (x != q2.size()-1) {
                    cout << ",";
                }
            }
            cout << endl;
        }
        return deserialize(q);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
