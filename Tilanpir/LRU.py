import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._data = collections.OrderedDict()
        self._capacity = capacity
        
        

    def get(self, key):
        """
        :rtype: int
        """
        #If key does not exist, we want it to throw exception
        try:
            valueForReturn = self._data[key]
        except KeyError:
            print "This key does not exist"
            return 
        del self._data[key]
        self._data[key] = valueForReturn
        return valueForReturn
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self._data:
            del self._data[key]
            self._data[key] = value
            return
        if len(self._data) == self._capacity:
            self._data.popitem(last = False)
        self._data[key] = value
        return



#test:
if __name__ == "__main__":
    cache = LRUCache(9)
    cache.set(9, "val1")
    v = cache.get(8)
    print v
