class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            diffCounter = 0
            for i in range(0, len(t)):
                if s[i] != t[i]:
                    diffCounter += 1
                if diffCounter > 1:
                    return False
            return diffCounter == 1
        else:
            if abs(len(s) - len(t)) != 1:
                return False
            #make s the longer one
            if len(s) < len(t):
                s, t = t, s
            temp = None
            for i in range(0, len(t)):
                if t[i] != s[i]:
                    temp = t[:i] + s[i] + t[i:]
                    break
            if not temp: return True
            return temp == s

#test:
if __name__ == "__main__":
    sol = Solution()
    s = "abcdefg"
    t = "abcKefgds"
    print sol.isOneEditDistance(s, t)
