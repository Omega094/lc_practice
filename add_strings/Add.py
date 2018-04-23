class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = map(int, num1)
        l2 = map(int, num2)
        l1.reverse()
        l2.reverse()
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        result = [0]*(len(l1)+1)
        for i in xrange(0, len(l1)):
            if i  < len(l2):
                s = l1[i] + l2[i]
            else:
                s = l1[i]
            result[i] += s
            result[i+1] += (result[i]  //10)
            result[i] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        answer = "".join(map(str, result))
        return answer
            
        
