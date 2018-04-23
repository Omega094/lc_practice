class Solution(object):

    def minWindow(self, s, t):
        tLst = list(set(list(t)))
        from collections import Counter
        charDict = Counter(tLst)
        for char in charDict:
            charDict[char] = 0
        front = 0
        back = 0
        minStr = s
        while front != len(s):
            while 0 in charDict.values() :
                if s[front] in charDict:
                    charDict[s[front]] += 1
                front += 1
            while min( charDict.values() ) >= 1:
                if front - back + 1 < len(minStr):
                    minStr = s[back: front]
                #     print minStr, "minStr"
                # print s[back], "back"
                if s[back] in charDict:
                    charDict[s[back]] -= 1
                back += 1
        return minStr

    def minWindow_elegant(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        start = 0
        I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while start < j and need[s[start]] < 0:
                    need[s[start]] += 1
                    start += 1
                if not J or j - start <= J - I:
                    I, J = start, j
        return s[I:J]


#test:
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print sol.minWindow(s, t)
