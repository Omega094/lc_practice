import math
class Solution(object):
    
    def nCr(self ,n, r):
        #import math
        f = math.factorial
        return f(n)/f(r)/f(n-r)
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex = rowIndex + 1
        if rowIndex == 1: return [1]
        answer = []
        for i in range (1, rowIndex+1):
            #print i
            answer.append(self.nCr(rowIndex-1, i-1))
        return answer


#test
if __name__ == "__main__":
    sol = Solution()
    for i in range(0, 6):
        print sol.getRow(i)
