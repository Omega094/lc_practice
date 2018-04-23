from collections import deque
#O(n) for push, space optimal.
#Otherwise need to use pointer , which gives time optimal but sacrifices space. 
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for i in xrange(0, len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty(): return None
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.empty(): return None
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        
        
        
