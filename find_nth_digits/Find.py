class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
     
        currentReduce = 9
        currentReduceScale = 1
        digits = 1
        while currentReduce*digits < n:
            n -= currentReduce*digits
            currentReduce *= 10
            digits += 1
            currentReduceScale *= 10
   
  
        num =  currentReduceScale + (n-1)//digits 
        #print num, digits, n
 
        return int(str(num)[(n-1) % digits ])
