
1-liners Python

https://leetcode.com/problems/strobogrammatic-number/discuss/67203

* Lang:    python3
* Author:  StefanPochmann
* Votes:   19

My maybe best:

    def isStrobogrammatic(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))

Some others:

    def isStrobogrammatic(self, num):
        return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))

    def isStrobogrammatic(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)))

    def isStrobogrammatic(self, num):
        return all(map('696 00 11 88'.count, map(operator.add, num, num[::-1])))

    def isStrobogrammatic(self, num):
        return all(p in '696 00 11 88' for p in map(operator.add, num, num[::-1]))

    def isStrobogrammatic(self, num):
        return set(map(operator.add, num, num[::-1])) <= set('69 96 00 11 88'.split())

    def isStrobogrammatic(self, num):
        return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}

    def isStrobogrammatic(self, num):
        return set(map(''.join, zip(num, num[::-1]))) <= {'69', '96', '00', '11', '88'}
