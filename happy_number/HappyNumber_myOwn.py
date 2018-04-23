class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numSet = set()
        while n != 1:
            temp = 0
            while n != 0:
                temp += (n%10)**2
                n /= 10
            if temp in numSet: return False
            numSet.add(temp)
            n = temp
        return True
        
