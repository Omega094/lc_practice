class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        return self.KMP(haystack, needle)
    
    def getPrefix(self, pattern):
        j = -1
        prefix = [-1]*len(pattern)
        for i, c in enumerate(pattern):
            while j >-1 and pattern[j+1] != pattern[i] :
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    def KMP(self, text, pattern):
        j = -1
        prefix = self.getPrefix(pattern)
        for i , c in enumerate(text):
            while j >-1 and pattern[j+1] != text[i]:
                j = prefix[j]
            if pattern[j+1] == text[i]:
                j += 1
            if j == len(pattern) -1 :
                return i - j
        return -1

