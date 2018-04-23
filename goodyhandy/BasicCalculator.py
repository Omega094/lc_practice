class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = [1,1]
        result = 0
        start = 0
        current = ""
        sLst = []
        s = s.strip()
        while start < len(s):
            if s[start]  == " ": 
                start += 1
                continue
            if s[start].isdigit():
                current += s[start]
            else:
                if current != "":
                    sLst.append(current)
                    current = ""
                sLst.append(s[start])
            start += 1
        if current != "":
            sLst.append(current)
        frontPtr = 0
        while frontPtr < len(sLst):
            if sLst[frontPtr].isdigit():
                result += int(sLst[frontPtr]) * sign.pop()
            elif sLst[frontPtr] == "(":
                sign.append(sign[-1])
            elif sLst[frontPtr] == ")":
                sign.pop()
            elif sLst[frontPtr] == "+":
                sign.append(1*sign[-1])
            else:
                sign.append(-1*sign[-1])
            frontPtr += 1
        return result

#test
sol = Solution()
print sol.calculate("2-(5-6)")
