#Let's ignore n,
#The ith the number of time it is toggleed is the number of distinct divisors it has. 
#Use mathematics to prove it !
#For a number, a divisor appears in pair. 
#However, for Square Number, its divisors are odd. 

#Time O(1)
#Space O(1)

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
