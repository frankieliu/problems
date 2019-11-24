In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1169.invalid-transactions.algorithms.json

Brute force solution

https://leetcode.com/problems/invalid-transactions/discuss/366356

* Lang:    python
* Author:  keyvank1
* Votes:   28

The brute force worked during the exam time. We had to synthesize the given input vector of strings and break them into pieces that can be analyzed for the further conditions that exist in the problem.
The code goes as below. 
Time complexity: ```O(n^2)```
Space complexity: ```O(n)```
```
struct info{
    string name;
    int price;
    int time;
    string city;
};
class Solution {
public:
    vector<string> invalidTransactions(vector<string>& t) {
        
        vector<info> tmod;
        string st = "";
        info temp;
        int count;
        for (int i = 0 ;i<t.size();i++){
            count = 0;
            for (int j = 0;j<t[i].size();j++){
                if (t[i][j]==\',\'){
                    if (count==0)
                        temp.name = st;
                    if (count==1)
                        temp.time = stoi(st);
                    if (count==2)
                        temp.price = stoi(st);
                    count++;
                    st = "";
                    continue;
                }
                st+=t[i][j];
            }
            temp.city = st;
            tmod.push_back(temp);
            st = "";
        }
		
        vector<string> ret;
        bool found = false;
		//The brute force search of O(n^2) is as follows
        for (int i = 0;i<tmod.size();i++){
            insrt = false;
            if (tmod[i].price>=1000){
                ret.push_back(t[i]);
                continue;
            }
            for (int j = 0;j<tmod.size();j++){   
                if (i == j) continue;
                if (tmod[i].name==tmod[j].name && (abs)(tmod[i].time-tmod[j].time)<=60 && tmod[i].city!=tmod[j].city){
                    found = true;
                    break;
                }
            }
            if (found){
                ret.push_back(t[i]);
                found = false;
            }
        }
        return ret;
    }
};
```

