# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.lastBuf = None
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        alreadyRead = 0
        flag = False
        while alreadyRead < n:
            if self.lastBuf :
                tempBuf , thisRead= self.lastBuf
                self.lastBuf = None
                flag = True
            else:
                tempBuf = ['']*4
                thisRead = read4(tempBuf)
                flag = False
            toRead = min(4,thisRead )
            for i in xrange(0, toRead):
                buf[alreadyRead] = tempBuf[i]
                alreadyRead += 1
                if alreadyRead == n :
                    if i != toRead-1:
                        self.lastBuf = (tempBuf[i+1:], toRead - i -1)
                    return alreadyRead
            if thisRead < 4 and not flag: break
        return alreadyRead
        
        
        
