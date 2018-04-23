class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = map(int, list(num1))
        num2 = map(int, list(num2))
        num1.reverse()
        num2.reverse()
        result = [0 for _ in xrange(len(num1) +len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                val = num1[i]*num2[j] 
                result[i+j] += val
                result[i + j + 1] += result[i+j] // 10
                #don't forget to mod it by ten 
                result[i+j] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result = map(str,result)
        result.reverse()
        return "".join(result)
#test
sol = Solution()
print sol.multiply('890','982')
