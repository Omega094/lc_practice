class Solution(object):
    def isValid(self, parens):
        if not parens: return True
        stack = []
        left = "({["
        right = ")}]"
        pair= {"(":")","[":"]","{":"}" }
        for p in parens:
            if p in left: stack.append(p)
            else:
                if not stack: return False
                else: 
                    p_left = stack.pop()
                    if pair[p_left] != p:
                        return False
        return not stack

    def isValidConstantSpace(self, s):
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')

        if s == '':
            return True
        else:
            return False
#test 
if __name__ == "__main__":
    sol = Solution()
    p1 = "{([])}"
    p2 = "((())))))"
    print sol.isValid(p1)
    print sol.isValid(p2)
    print sol.isValidConstantSpace(p1)
    print sol.isValidConstantSpace(p2)
        
