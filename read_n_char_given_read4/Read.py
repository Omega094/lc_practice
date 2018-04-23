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
    
        charAlreadyRead = 0
        charToRead = n
        while charToRead > 0:
            tempBuf = [''] * 4
            read_num = min(read4(tempBuf), charToRead)
            for i in range(0, read_num):
                buf[charAlreadyRead+i] = tempBuf[i]
            charAlreadyRead += read_num
            charToRead -= read_num
            if read_num < 4:
                break
        return charAlreadyRead
