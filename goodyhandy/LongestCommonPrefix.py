class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        shortestStr = min(strs, key = len)
        currentShortest = shortestStr
        for word in strs:
            temp = ""
            for i, c in enumerate(shortestStr):
                if c != word[i]: break
                temp += c
            currentShortest = min( (temp, currentShortest), key = len)
        return currentShortest
