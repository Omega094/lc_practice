class Solution(object):
    #use a global var to cache each result in recursive call
    #so we can accerlerate a lot
    def __init__(self):
        self._localMem = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self._localMem.get(s) == True: return True
        for i in range(0, len(s)-1):
            if s[i:i+2] == "++":
                afterChange = s[:i] + '--' + s[i+2:]
                cacheResult = self._localMem.get(afterChange,self.canWin(afterChange))
                if not cacheResult :
                    self._localMem[s] = True
                    return True
                else:
                    self._localMem[afterChange] = True
        return False

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.canWin("++-----------++++++-----+-------------------------+-+-++++++")
