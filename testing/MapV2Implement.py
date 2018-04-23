import profile

class MapV2(object):

    def __init__(self):
        self._data = []
    
    #Add operation O(1)
    def add(self ,value):
        if value in self._data:
            return 
        self._data.append(value)
        return 
    
    #remove operation O(count)
    def remove(self, value):
        if value not in self._data:
            return 
        self._data.remove(value)
        return

    #Lookup operation O(count)
    def contains(self, value):
        return value in self._data
    
    #Clear operation O(1), just re-allocate a new array. 
    def clear(self):
        self._data = []
    
    #iterate operation, O(count)
    def iterate(self):
        for val in self._data:
            print val
        print self._data



#test:
if __name__ == "__main__":
    map_v2 = MapV2()
    map_v2.add(2)
    map_v2.add(0)
    map_v2.add(1)
    print map_v2.contains(9)
    print map_v2.contains(2)
    map_v2.iterate()

