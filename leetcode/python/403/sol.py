
Elegant Python Simple Solution

https://leetcode.com/problems/frog-jump/discuss/88887

* Lang:    python3
* Author:  vimukthi
* Votes:   0

    class Solution(object):
        def canCross(self, stones):
            map = {val:idx for idx, val in enumerate(stones)}
            visited = {}
            return self.jump(1, 1, stones[-1], map, visited)
    
        
        def jump(self, current, last_step, goal, map, visited):
            if current not in map:
                return False
            if current == goal:
                return True
            if (current, last_step) in visited:
                return visited[(current, last_step)]
            can_go_forward = False    
            for next_step in [last_step - 1, last_step, last_step + 1]:
                if next_step > 0:
                    can_go_forward = can_go_forward or self.jump(current + next_step, next_step, goal, map, visited)
            visited[(current, last_step)] = can_go_forward
            return can_go_forward
