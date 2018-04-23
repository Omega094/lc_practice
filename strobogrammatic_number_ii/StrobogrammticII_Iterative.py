class Solution(object):
    
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairDict = {"1": "1", "8": "8", "6": "9", "9":"6", "0":"0"}
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
                    newSol.append(key+s+val)
            solutionList = newSol
            mid -= 1
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.findStrobogrammatic(5)
