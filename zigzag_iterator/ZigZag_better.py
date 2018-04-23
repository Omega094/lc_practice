class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.data = [(len(v),iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append(((len-1), iter))
        return next(iter)
    
    def hasNext(self):
        return bool(self.data)

#test:
if __name__ == "__main__":
    zigzag = ZigzagIterator([1,2],[3,4])
    while zigzag.hasNext():
        print zigzag.next()
