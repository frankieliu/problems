In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1078.occurrences-after-bigram.algorithms.json

C++ Search for Bigram

https://leetcode.com/problems/occurrences-after-bigram/discuss/308314

* Lang:    python
* Author:  votrubac
* Votes:   11

First, compose our bigram as ```first + " " + second + " "```. Thanks [alreadydone](https://leetcode.com/alreadydone/) for the advice to add an extra space in the end.  

Then search for all bigram occurrences, extracting the word that follows.
```
vector<string> findOcurrences(string text, string first, string second) {
  vector<string> res;
  auto bigram = first + " " + second + " ";
  auto p = text.find(bigram);
  while (p != string::npos) {
    auto p1 = p + bigram.size(), p2 = p1;
    while (p2 < text.size() && text[p2] != \' \') ++p2;
    res.push_back(text.substr(p1, p2 - p1));
    p = text.find(bigram, p + 1);
  }
  return res;
}
```
# Complexity Analysis
Runtime: *O(n + m)*, where *n* is the size of the string, and *m* - size of the bigram. 
> A single find operation is *O(n + m)*; we can search several times but we move forward and don\'t consider the part we searched already.
> 
> Even if our string is ```"a a a a ..."```, and bigram - ```"a a "```, the total number of operation will not exceed *2n*.  

Memory: *O(m)* to store the bigram, or *O(n)* if we consider the memory for the result.
