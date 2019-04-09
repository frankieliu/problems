
My Python Solution

https://leetcode.com/problems/flatten-2d-vector/discuss/67653

* Lang:    python3
* Author:  yinfeng.zhang.9
* Votes:   14

    class Vector2D:
        # Initialize your data structure here.
        # @param {integer[][]} vec2d
        def __init__(self, vec2d):
            self.col = 0
            self.row = 0
            self.vec = vec2d
            
        # @return {integer}
        def next(self):
            result = self.vec[self.row][self.col]
            self.col += 1
            return result
    
        # @return {boolean}
        def hasNext(self):
            while self.row < len(self.vec):
                if self.col < len(self.vec[self.row]):
                    return True
                
                self.col = 0
                self.row += 1
                
            return False
