class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0]*(len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                product = int(num1[i])*int(num2[j])
                temp = result[i+j] + product
                result[i+j] = temp%10
                result[i+j+1]  += temp/10
        #print result 
        result.reverse()
        answer = "".join(map(str, result)).lstrip("0")
        return "0" if answer =="" else answer
