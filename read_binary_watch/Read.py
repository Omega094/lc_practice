import copy
class Solution(object):

    def checkValid(self, h, m):
        return  0 <= h <= 11 and 0 <= m <= 59
            
    def toTime(self, digitSet):
        digits = copy.deepcopy(digitSet)
        hour = 0
        minute = 0
        for h in xrange(7, 11):
            if h in digits:
                hour += 2**(h-7)
                digits.remove(h)
        for m in xrange(1, 7):
            if m in digits:
                minute += 2**(m - 1)
                digits.remove(m)
        return (hour, minute)
    
    def generateCombination(self, n, digitSet, currentMax, solutionList):
        if len(digitSet) == n:
            h, m  = self.toTime(digitSet)
            if self.checkValid(h, m ):
                mStr = str(m)
                if m < 10:
                    mStr = "0"+mStr
                solutionList.append(str(h)+":"+mStr)
            return 
        for i in xrange(currentMax + 1, 11):
            digitSet.add(i)
            self.generateCombination(n,digitSet, i, solutionList) 
            digitSet.remove(i)
            
        return 


    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        solutionList = []
        self.generateCombination(num, set(), 0, solutionList)
        return solutionList

#test
sol = Solution()
print sol.readBinaryWatch(1)

        
        
