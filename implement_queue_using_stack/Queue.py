#Using two stacks. 
#It is amotized O(1) and space optimal !!
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack , self.outstack = [], []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)
        
    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty(): return
        self.move()
        return self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.empty(): return None
        self.move()
        return self.outstack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.instack and not self.outstack
        
