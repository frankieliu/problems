
Python, 5 lines, O(n) time, O(n) space

https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/103658

* Lang:    python3
* Author:  Matti
* Votes:   1

```
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {rest : i for i, rest in enumerate(list1)}
        dict2 = {rest : i for i, rest in enumerate(list2)}
        dictSum = {rest : dict1[rest]+dict2[rest] for rest in dict1 if rest in dict2}
        minSum = min(dictSum.values())
        return [key for key in dictSum if dictSum[key] == minSum]
```
Or a little bit faster solution:
```
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {rest : i for i, rest in enumerate(list1)}
        dict2 = {rest : i for i, rest in enumerate(list2)}
        dictSum = {rest : dict1[rest]+dict2.get(rest, 2017) for rest in dict1}
        minSum = min(dictSum.values())
        return [key for key in dictSum if dictSum[key] == minSum]
```
The fourth line in both solutions could be in the last one (```return [key for key in dictSum if dictSum[key] == min(dictSum.values())```), but that makes it slower. Is that because it calculates the min again every iteration?
