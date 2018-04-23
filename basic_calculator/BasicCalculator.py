class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 #record the digit
        #Add one more 1 just in case of like (1+2) 
        signs = [1, 1]
        total = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop()*int(s[start:i])
                continue
            if c in "+-(":
                signs += [signs[-1]*(1, -1)[c == '-']]
            elif c == ')':
                signs.pop()
            i += 1
        return total

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.calculate("(1+(4+5+2)-3)+(6+8)")
