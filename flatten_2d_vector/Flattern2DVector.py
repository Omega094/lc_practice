iclass Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d
        self.current = 0
        self.current_ptr = 0
        self.skipEmptyList()
        
    def skipEmptyList(self):
        while self.current < len(self.data) and self.data[self.current] == []:
            self.current += 1
        return 

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        value = self.data[self.current][self.current_ptr]
        if self.current_ptr == len(self.data[self.current])-1:
            self.current_ptr = 0
            self.current += 1
            self.skipEmptyList()
        else:
            self.current_ptr += 1 
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current < len(self.data)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
