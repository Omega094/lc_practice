class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._topPointer = -1
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._topPointer += 1
        if self._topPointer >= len(self._data) :
            self._data.append(x)
        else:
            self._data[self._topPointer] = x
        return 
    
        

    def pop(self):
        """
        :rtype: nothing
        """
        #Return or throw exception
        if self.empty(): return
        val = self.top()
        self._topPointer -= 1

    def top(self):
        """
        :rtype: int
        """
        return self._data[self._topPointer]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self._topPointer == -1
