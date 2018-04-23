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
        from collections import deque
        self.width = width
        self.height = height
        self.food = map(tuple, food[::-1])
        self.pathSet = set([(0,0)])
        self.pathQueue = deque([(0,0)])
        self.position = (0,0)

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == 'R':
            self.position = (self.position[0],self.position[1]+1)
        elif direction == 'D':
            self.position = (self.position[0]+1,self.position[1])
        elif direction == 'U':
            self.position = (self.position[0]-1,self.position[1])
        else :
            self.position = (self.position[0],self.position[1]-1)
        if self.food and self.position == self.food[-1]:
            self.pathQueue.append(self.position)
            self.pathSet.add(self.position)
            self.food.pop()
            return len(self.pathQueue)-1
        poped = self.pathQueue.popleft()
        self.pathSet.remove(poped)
        self.pathQueue.append(self.position)
        if self.position in self.pathSet or self.position[1] >= self.width or self.position[0] >= self.height or self.position[0]<0 or self.position[1] < 0 :
            return -1
        self.pathSet.add(self.position)
        return len(self.pathQueue) -1 


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
