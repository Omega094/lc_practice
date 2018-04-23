class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messageToTime = dict()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false. The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.messageToTime.has_key(message) and self.messageToTime[message] > timestamp - 10:
            return False
        self.messageToTime[message] = timestamp 
        return True
    
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
