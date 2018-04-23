# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        charAlreadyRead = 0
        while self.queue and n > 0:
            buf[charAlreadyRead] = self.queue.pop(0)
            charAlreadyRead += 1
            n -= 1
        
        while n > 0:
            buff4 = ['']*4
            singleReadLength = read4(buff4)
            if not singleReadLength:
                return charAlreadyRead
                
            #Put the extra non-needed into the queue
            #For this call, we don't need them 
            if singleReadLength > n:
                self.queue += buff4[n:singleReadLength]
            
            #Write buff4 into buf
            
            for i in range(min(singleReadLength, n)):
                buf[charAlreadyRead] = buff4[i]
                charAlreadyRead += 1
                n -= 1
        return charAlreadyRead

