class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3: return True
        #O(1) time solution can be derived by the following code 
        
        # preTable =[ True, True, True]
        # for i in xrange(3, n):
        #     result = False
        #     for j in range(2, -1, -1):
        #         if preTable[j] == False:
        #             result = True
        #             break
        #     preTable = preTable[1:] + [result]
        # return preTable[-1]
        
        return n % 4 != 0
#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.canWinNim(1348820612)
