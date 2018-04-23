class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        from collections import deque
        v1 = deque(v1)
        v2 = deque(v2)
        self.data = deque()
        while v1 or v2:
            if v1:
                self.data.append(v1.popleft())
            if v2:
                self.data.append(v2.popleft())
        return
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.data.popleft()
        return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.data) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
