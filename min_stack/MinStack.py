class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._minData = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        if not self._minData or self._minData[-1] >= x:
            self._minData.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        top = self._data.pop()
        if top == self._minData[-1]:
            self._minData.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self._data: return None
        return self._minData[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
