class Solution(object):
    def dfsHelper(self, currentResult, lastNum, currentStr, remainStr, solutionLst):
        #print currentResult, currentStr, remainStr
        if remainStr == "":
            if currentResult == self.target:
                solutionLst.append(currentStr)
            return
        for i in xrange(1, len(remainStr)+1):
            val = int(remainStr[:i])
            valStr = remainStr[:i]
            if i == 1 or (i > 1 and remainStr[0] != "0"):
                self.dfsHelper(currentResult + val, val, currentStr + '+' +valStr, remainStr[i:], solutionLst)
                self.dfsHelper(currentResult - val, -val, currentStr + '-' +valStr, remainStr[i:], solutionLst)
                self.dfsHelper(currentResult-lastNum+lastNum*val, val*lastNum, currentStr + '*' +valStr, remainStr[i:], solutionLst)
        return
    def addOperators(self, num, target):
        self.target = target
        solutionLst = []
        for i in xrange(1, len(num)+1):
            var = int(num[:i])
            if i == 1 or (i > 1 and num[0] != "0"):
                varStr = num[:i]
                self.dfsHelper(var, var, varStr, num[i:], solutionLst)
        return solutionLst

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.addOperators("123", 6)
