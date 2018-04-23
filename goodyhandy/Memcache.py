class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.data = {}
        self.INF = 2147483647 
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if not self.data.has_key(key) or self.data[key][1] < curtTime:
            return self.INF
        return self.data[key][0]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl == 0:
            self.data[key] = [value, self.INF]
        else:
            self.data[key] = [value, curtTime + ttl - 1]
        return 
        
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        del self.data[key]
        return 
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if not self.data.has_key(key) or self.data[key][1] < curtTime:
            return self.INF
        self.data[key][0] += delta
        return self.data[key][0]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if not self.data.has_key(key) or self.data[key][1] < curtTime:
            return self.INF
        self.data[key][0] -= delta
        return self.data[key][0]

