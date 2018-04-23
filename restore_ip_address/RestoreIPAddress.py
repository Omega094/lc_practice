class Solution(object):

    def getIDSearchHelper(self, s, currentIndex, currentIP, currentAddressNum, solutionList):
        #Base valid cases
        if currentAddressNum == 4:
            if currentIndex == len(s):
                # print currentIP
                # print currentIndex, "This is currentIndex"
                solutionList.append(currentIP)
            return
        #Base Invalid cases:
        if currentIndex >= len(s): return
        #Start recursive call
        for i in range(currentIndex + 1, currentIndex + 4):
            nextIPNum = s[currentIndex: i]
            # print nextIPNum
            if nextIPNum[0] == '0' and len(nextIPNum) > 1: continue
            if nextIPNum and int(nextIPNum) >= 0 and int(nextIPNum) < 256:
                self.getIDSearchHelper(s, i, currentIP + '.' + nextIPNum, currentAddressNum+1, solutionList)
            else:
                continue
        return

    
    def restoreIpAddresses(self, s):
        solutionList = []
        self.getIDSearchHelper(s, 0, '', 0, solutionList)
        for i, solution in enumerate(solutionList):
            solution = solution[1:]
            solutionList[i] = solution
        return solutionList

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.restoreIpAddresses('25525511135')
