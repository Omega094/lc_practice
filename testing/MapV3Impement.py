import profile

class MapV3(object):

    def __init__(self, size):
        #Pre allocate an random access array
        self._size = size 
        self._data_pointer = [None for _ in range(size)]
        self._data = []
        self._counter = 0

    #Add operation O(1)
    def add(self ,value):
        if value >= self._size:
            return 
        #This means the map has been cleaned.  
        index = self._data_pointer[value]
        if index and index < counter and self._data[index] == value:
                return
        self._data_pointer[value] = self._counter
        self._data.append(value)
        self._counter += 1
        return 
    
    #remove operation O(1)
    def remove(self, value):
        #Value does not exist or value larger than max size
        if value >= self._size or self._data_pointer[value] == None:
            print "This value does not exist."
            return
        index = self._data_pointer[value]
        #Value exist but it might be caused by clearing the map.
        if index >= self._counter or self._data[index] != value:
            return
        #Swap with the latest element
        self._data[index] = self._data[self._counter-1]
        latestValue = self._data[index]
        self._data_pointer[latestValue] = index
        self._data_pointer[value] = None
        self._data.pop()
        self._counter -= 1
        return

    #Lookup operation O(1)
    def contains(self, value):
        if value >= self._size or self._data_pointer[value] == None: return False
        index = self._data_pointer[value]
        #Need to make sure the value on the index is correct.
        return index < self._counter and self._data[index] == value
    
    #Clear operation O(1) 
    def clear(self):
        self._counter = 0
        self._data = []

    
    #iterate operation, O(size)
    def iterate(self):
        for val in self._data:
            print val

#test:
if __name__ == "__main__":
    map_v3 = MapV3(9)
    map_v3.add(2)
    #map_v3.add(0)
    #map_v3.add(1)
    #map_v3.remove(0)
    map_v3.clear()
    map_v3.add(1)
    print map_v3.contains(9)
    print map_v3.contains(2)
    print map_v3.contains(1)
    map_v3.iterate()

