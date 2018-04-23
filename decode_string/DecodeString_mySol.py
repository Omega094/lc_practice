class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        digitMap = defaultdict(int)
        strMap = defaultdict(str)
        k = 0
        for c in s:
            if c.isdigit():
                digitMap[k] = digitMap[k]*10 + int(c)
            elif c == "[":
                k += 1
            elif c == "]":
                strMap[k-1] += digitMap[k-1]*strMap[k]
                digitMap[k-1] = 0
                strMap[k] = ""
                k -= 1
            else:
                strMap[k] += c
        return strMap[0]
