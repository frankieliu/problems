
C++ Concise and Clean Implementation Using a Shared Traverse Function.

https://leetcode.com/problems/design-in-memory-file-system/discuss/103349

* Lang:    cpp
* Author:  fentoyal
* Votes:   0

It takes advantage of the assumptions the question give. So all traverse work can be combined to one single function.
```
class FileSystem {
    struct Node
    {
        string name, content;
        bool type = 0;//0 directory, 1 file
        map<string, Node *> children;
        Node (const string & _name = ""):name(_name){}
    } * root;
    Node * traverse(string const & path) {
        size_t last_pos = 1, cur_pos = 0;
        Node * cur_node = root;
        while(last_pos < path.size() && cur_pos != string::npos)
        {
            cur_pos = path.find_first_of('/', last_pos);
            string name = path.substr(last_pos, cur_pos - last_pos);
            last_pos = cur_pos + 1;
            cur_node = cur_node->children.emplace(name, new Node(name)).first->second;
        }
        return cur_node;
    }
public:
    FileSystem() {
        root = new Node();
    }
    vector<string> ls(string path) {
        vector<string> result;
        Node * cur_node = traverse(path);
        if (cur_node->type == 1)
            result.push_back(cur_node->name);
        else for (auto const & thepair : cur_node->children)
            result.push_back(thepair.first);
        return result;
    }
    void mkdir(string path) {
        traverse(path);
    }
    void addContentToFile(string path, string content) {
        Node * node = traverse(path);
        node->type = 1;
        node->content += content;
    }
    string readContentFromFile(string path) {
        return traverse(path)->content;
    }
};


```
