
Python Bisect Insort

https://leetcode.com/problems/exam-room/discuss/255053

* Lang:    python3
* Author:  joinyoung
* Votes:   0

Use a sorted list `self.occupied` to keep track of everyone\'s position. Everytime a new person comes in, find the best location between `left` and `right` and seat the person in `(left + right) // 2` using `bisect.insort()`. Don\'t forget the consider the positions before the first person `self.occupied[0]` and after the last person `self.occupied[-1]`.
```
class ExamRoom:
    def __init__(self, N: int):
        self.occupied = []
        self.N = N

    def seat(self) -> int:
        if not self.occupied: 
            self.occupied.append(0)
            return 0
        left, right = -self.occupied[0], self.occupied[0]
        maximum = (right - left) // 2
        for start, end in zip(self.occupied, self.occupied[1:] + [2 * self.N - 2 - self.occupied[-1]]):
            if (end - start) // 2 > maximum:
                left, right = start, end
                maximum = (right - left) // 2
        bisect.insort(self.occupied, left + maximum)
        return left + maximum
            
    def leave(self, p: int) -> None:
        self.occupied.remove(p)
```
