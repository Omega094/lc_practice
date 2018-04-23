
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(0, len(s)-1):
            if s[i:i+2] == "++":
                result.append(s[:i]+"--"+s[i+2:])
        return result 
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.generatePossibleNextMoves('++++')
