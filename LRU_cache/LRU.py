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
        if not self._data.has_key(key):
            return -1
        valueForReturn = self._data.get(key)
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




