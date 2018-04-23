class Solution(object):

    def isvalid(self,s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0

    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
             valid = filter(self.isvalid, level)
             if valid:
                 return valid
             level ={s[:i] + s[i+1:] for s in level for i in range(len(s))}
        return []

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.removeInvalidParentheses("()())()")
    print sol.removeInvalidParentheses("(a)())()")
