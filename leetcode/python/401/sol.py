
Easy Understand 46ms Python Solution With HashTable

https://leetcode.com/problems/binary-watch/discuss/88623

* Lang:    python3
* Author:  steven10
* Votes:   0

```python
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        up = 11
        down = 59
        up_hash = self.generateHash(up)
        down_hash = self.generateHash(down)
        n = num
        result = []
        while n >=0:
        	rest = num - n
        	hours = up_hash[n]
        	minutes = down_hash[rest]
        	for hour in hours:
        		for minute in minutes:
        			result.append('%d:%.2d'%(hour,minute))
        	n = n - 1
        return result

    def generateHash(self, num):
    	num_hash = collections.defaultdict(list)
        while num >= 0:
        	n = num
        	count = 0
        	while n > 0:
        		count = count + (n & 1)
        		n = n >> 1
        	num_hash[count].append(num)
        	num = num - 1
        return num_hash
```
