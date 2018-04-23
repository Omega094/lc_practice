class Solution(object):
        #The key idea is to only increment it from right. (Which makes the code looks easier.)
        #As long as l is <= right, we can always make it valid regardless of what it is now 
        #(Assume we have enough parentheses to use. 
        #If l > r, we can never make it valid.

    def helper (self, l, r, parens, solutionList):
        #Only case that we are not able to continue making the current pattern
        #to be valid
        if l > r : return
        if l == 0 and r == 0:
            solutionList.append(parens)
            return
        if l < 0 or r < 0: return
        #Create it only by appending
        self.helper(l-1, r, parens+"(", solutionList)
        self.helper(l, r-1, parens+")", solutionList)

    def generateParenthesis(self, n):
        solutionList = []
        self.helper(n, n, "", solutionList)
        return solutionList

#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.generateParenthesis(3)
        
