import threading
class singletonObj(object):
    _obj = None
    _lock = threading.Lock()

    def __init__(self, id):
        self._id = id 
        
    @classmethod
    def getInstance(cls, id):
        if not cls._obj:
            with cls._lock:
                if not cls._obj:
                    cls._obj = cls(id)
        return cls._obj

#test
a = singletonObj.getInstance(9)
b = singletonObj.getInstance(10)
print a._id, a
print b._id, b



