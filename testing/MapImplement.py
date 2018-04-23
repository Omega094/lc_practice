import profile

class MapV1(object):

    def __init__(self, size):
        #Pre allocate an random access array
        self._size = size 
        self._data = [None for _ in range(size+1)]
    
    #Add operation O(1)
    def add(self ,value):
        if value > self._size:
            return 
        self._data[value] = 1
        return 
    
    #remove operation O(1)
    def remove(self, value):
        if value > self._size:
            return 
        self._data[value] = None
        return

    #Lookup operation O(1)
    def contains(self, value):
        return value < self._size and self._data[value] != None
    
    #Clear operation O(size) 
    def clear(self):
        for i in range (0, self._size+1):
            self._data[i] = None
    
    #iterate operation, O(size)
    def iterate(self):
        for i in range (0, self._size+1):
            if self._data[i]:
                print i
        print self._data




#test:
if __name__ == "__main__":
    map_v1 = MapV1(9)
    map_v1.add(2)
    map_v1.add(0)
    map_v1.add(1)
    print map_v1.contains(9)
    print map_v1.contains(2)
    map_v1.iterate()

