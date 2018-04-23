class Solution(object):
    def findStrobogrammatic(self, n, lower = None, upper = None):
        if n == 1 and lower != None and upper != None:
            return len([i for i in ["1","8","0"] if int(i) >= int(lower) and int(i) <= int(upper)  ])
        pairDict = {"1": "1", "8": "8", "6": "9", "9":"6", "0":"0"}
        #This works when there is no bound 
        if lower == None and upper == None:
            currentResult = 1
            if n%2 == 1:
                currentResult = 3
                n-= 1
            mid = n/2
            return 4*(5**(mid-1))*currentResult
        solutionList = [""]
        if n%2 == 1:
            solutionList = ["1","8","0"]
            n-= 1
        mid = n/2
        while mid > 0 :
            newSol = []
            for key, val in pairDict.iteritems():
                if key == '0' and mid == 1: continue
                for s in solutionList:
                    result = key+s+val
                    if mid == 1:
                        if lower != None and int(result) < int(lower): continue
                        if upper != None and int(result) > int(upper): continue
                    newSol.append(result)
            solutionList = newSol
            mid -= 1

        
        return len(solutionList)
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        lenLow  = len(low)
        lenHigh = len(high)
        if lenLow < lenHigh:
            result = self.findStrobogrammatic(lenLow, low, None) + self.findStrobogrammatic(lenHigh, None, high)
            for i in range (lenLow+1, lenHigh):
                result += self.findStrobogrammatic(i)
        else:
            result = self.findStrobogrammatic(lenLow, low, high)
        return result 
