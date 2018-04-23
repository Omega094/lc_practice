class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "": return 0
        if haystack == "": return -1
        if len(needle) > len(haystack): return -1
        if haystack == needle: return 0
        needleLen = len(needle)
        for i in range (0, len(haystack) - len(needle) + 1):
            if haystack[i:needleLen] == needle:
                return i
        return -1



#test 

