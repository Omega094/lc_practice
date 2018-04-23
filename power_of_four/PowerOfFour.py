class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        counter = 0
        while num != 0:
            if num & 1 == 1 and num != 1: return False
            counter += 1
            num = num >> 1
        return counter %2 == 1


