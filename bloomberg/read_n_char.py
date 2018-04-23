# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        alreadyRead = 0
        while alreadyRead < n:
            tempBuf = ['']*4
            thisRead = read4(tempBuf)
            for i in xrange(0, min(4,thisRead )):
                buf[alreadyRead] = tempBuf[i]
                alreadyRead += 1
                if alreadyRead == n : return alreadyRead
            if thisRead < 4: break
        return alreadyRead
