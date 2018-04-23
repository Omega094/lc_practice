from collections import deque
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.maxNum = maxNumbers
        self.recycled = deque()
        self.used = set()
        self.currentMax = 0

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.used) == self.maxNum: return -1
        val = self.currentMax
        if self.recycled:
            val = self.recycled.popleft()
        else:
            self.currentMax += 1
        self.used.add(val)
        return val
            

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number not in self.used and number < self.maxNum

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number not in self.used: return
        self.used.remove(number)
        self.recycled.append(number)
        return
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
