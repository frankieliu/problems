
Easy python solution

https://leetcode.com/problems/design-snake-game/discuss/82744

* Lang:    python3
* Author:  wuchjie
* Votes:   1

Here is a very simple python code. 

I use a queue to simulate the snake and use a set to keep all parts of the snake body.
Each move we will first pop the tail, get the head, and get the new head based on the direction.
If the new head come cross the body or get out of the boundary, it will return -1.
We enqueue the new head, add the new head to the body set.
If the new head meets the food, we will put the tail back. Notice the axises of positions of the food are reversed ([1,2] is actually [2,1]).

    class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.foodIndex=0
        self.snake=collections.deque() #A queue as the snake
        self.snake.append((0,0))
        self.body={(0,0)} #A set to keep all positions of the snake
        self.foods=food
        self.width=width
        self.height=height
        self.moves={'U':(0,-1),'L':(-1,0),'R':(1,0),'D':(0,1)}


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        tail=self.snake.popleft() #pop out the tail
        self.body.remove(tail)
        if not self.snake:
            head=tail
        else:
            head=self.snake[-1]
        xm,ym=self.moves[direction]
        nx,ny=head[0]+xm,head[1]+ym
        if (nx,ny) in self.body or nx<0 or nx>=self.width or ny<0 or ny>=self.height:
            return -1
        self.snake.append((nx,ny)) #append the new head
        self.body.add((nx,ny))
        if self.foodIndex<len(self.foods) and nx==self.foods[self.foodIndex][1] and ny==self.foods[self.foodIndex][0]:
            self.foodIndex+=1
            self.snake.appendleft(tail)
            self.body.add(tail)
        #Add back the tail if the snake eat a food
        return len(self.snake)-1
