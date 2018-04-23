class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        table = [ False for _ in xrange(len(s))]
        for i in xrange(len(s)):
            if s[:i+1] in wordDict:
                table[i] = True
                continue 
            #From end is faster
            for j in xrange(i, 0, -1):
                if s[j:i+1] in wordDict and table[j-1] == True:
                    table[i] = True
                    break
        return table[-1]
