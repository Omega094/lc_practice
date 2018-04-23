class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        resultSet = set()
        recordSet = set()
        for i in range (0, len(s)- 9):
            if s[i: i+10] in recordSet:
                resultSet.add(s[i:i+10])
            else:
                recordSet.add(s[i:i+10])
        return list(resultSet)

#test:
if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    sol = Solution()
    print sol.findRepeatedDnaSequences(s)
