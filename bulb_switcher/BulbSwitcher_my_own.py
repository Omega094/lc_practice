class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        count = 0
        i= 1
        while i**2 <=n :
            count += 1
            i += 1
        return count
