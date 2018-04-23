import profile 

class EfficientSet(object):

    def __init__(self, size):
        self._counter = 0
        self._data = []
        self._size = size
        self._data_pointer = [None for _ in range(size)]

    #O(1) clear 
    def clear(self):
        self._counter = 0
        self._data = []

    #O(1) time add
    def add(self, value):
        if value >= self._size:
            print "Value too large ."
            return
        #Value might already exist
        #Two cases :
        #Case 1: exist but is added into again. 
        """
        index = self._data_pointer[value]
        if index and index < self._counter :
            return 
        """
        #Case 2: exist but the self._data has been cleared. 
        #For example 
        #add(1) clear() then add(2)
        #Now both value 2 and 1 points to same index 
        #Therefore we need to check if self._data[index] == value,
        #If it is true just return, otherwise, we just re-assign value .
        #Let's comment out the code above 
        index = self._data_pointer[value]
        if index and index < self._counter and self._data_pointer[index] == value:
            return 
        #/////////////////////////
        self._data_pointer[value] = self._counter
        self._data.append(value)
        self._counter += 1
        return

    #O(1) time lookup 
    def contains(self, value):
        if value >= self._size or self._data_pointer[value] == None :
            return False
        #We need to check the same thing as we do for add()
        index  = self._data_pointer[value]
        return index < self._counter and self._data[index] == value
    
    #O(1) time remove
    def remove(self, value):
        if not self.contains(value):
            print "Value does not exist"
            return
        index = self._data_pointer[value]
        #Same as add()
        #Value exist but it is caused by clearing the map
        if index >= self._counter or self._data[index] != value:
            print "value does not exist"
            return 
        #This part can be trickty
        #We need to swap the removed element index with the latest element 
        self._data[index]  = self._data[self._counter -1 ]
        latestElement = self._data[index]
        self._data_pointer[latestElement] = index
        self._data_pointer[value] = None
        self._data.pop()
        self._counter -= 1
        return 

    #O(count) iterate
    def iterate(self):
        for num in self._data:
            print num
        return 

#test
if __name__ == "__main__":
    thisSet = EfficientSet(9)
    thisSet.add(2)
    thisSet.clear()
    thisSet.add(1)
    thisSet.add(9)
    print thisSet.contains(9)
    print thisSet.contains(2)
    print thisSet.contains(1)
    thisSet.iterate()




    
    
