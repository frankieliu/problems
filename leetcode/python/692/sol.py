
Python3 Solution, 9 lines, 85ms

https://leetcode.com/problems/top-k-frequent-words/discuss/108386

* Lang:    python3
* Author:  Root7
* Votes:   0


```
class Solution:
    def topKFrequent(self, words, k):
        fre, res = collections.defaultdict(list), []     
        for i,j in collections.Counter(words).most_common():
            fre[j].append(i)   
            
        for _ in range(k):
            while not fre[max(fre.keys())]:
                fre.pop(max(fre.keys()))
            fre[max(fre.keys())].sort()
            res.append(fre[max(fre.keys())].pop(0))               
        return res
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
    ```
