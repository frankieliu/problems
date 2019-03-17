
Python with hash table and detailed explaination

https://leetcode.com/problems/distribute-candies/discuss/102917

* Lang:    python3
* Author:  yang_fan
* Votes:   0

It's a regular hash solution. 
Go through all the candies and save each kind and the number into a dictionary. 
Then compare the total number of candy kind and half of the candies number, since the sister and brother should get equal number of candies. 
If the kind number is bigger than the half of the array, we should report the half of array. 
```
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dt={}
        n=len(candies)
        for candy in candies:
            dt[candy]=dt.get(candy,0)+1
        kinds=len(dt.keys())
        if kinds>n/2:
            return n/2
        else:
            return kinds
```
