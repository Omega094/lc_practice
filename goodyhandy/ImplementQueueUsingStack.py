class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackForPush = []
        self.stackForPop = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stackForPush.append(x)
        return 
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty(): return 
        if self.stackForPop:
            return self.stackForPop.pop()
        else:
            while self.stackForPush:
                self.stackForPop.append(self.stackForPush.pop())
        return self.stackForPop.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.empty() : return
        if self.stackForPop: return self.stackForPop[-1]
        return self.stackForPush[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stackForPush) + len(self.stackForPop) == 0
        
