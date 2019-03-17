
Python solution with Counter and GCD, beats 97% in time and 93% in space

https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/discuss/240959

* Lang:    python3
* Author:  BrianWong
* Votes:   0

class Solution:
    def hasGroupsSizeX(self, deck: \'List[int]\') -> \'bool\':
        n = len(deck)
        if n < 2: return False
        
        dic = collections.Counter(deck).values()
        
        l = len(dic)
        if l == 1: return True
        
        count = [value for value in dic]
        
        def gcd(x, y):
            if x > y: x, y = y, x
            if y%x == 0: 
                return x
            else:
                return gcd(x, y%x)
        
        
        temp = gcd(count[0], count[1])
        for i in range(2, l):
            temp = gcd(temp, count[i])
            if temp < 2: 
                return False
        
        return True
