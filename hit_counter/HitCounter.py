class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [(0,0)]*300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        index = (timestamp-1) % 300
        count, ts = self.arr[index]
        if ts == timestamp:
            count += 1
        else:
            count = 1
        self.arr[index] = count ,timestamp

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for c , ts in self.arr:
            if timestamp - ts < 300:
                count += c
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
