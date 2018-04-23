class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self._numDict = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self._numDict:
            self._numDict[number] += 1
        else:
            self._numDict[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self._numDict:
            if value - num not in self._numDict: continue
            if value - num != num or (value - num == num and self._numDict[num] > 1):
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
