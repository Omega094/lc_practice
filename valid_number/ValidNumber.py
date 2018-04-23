class Solution(object):

    def isNumber(self, s):
        INVALID = 0
        SPACE = 1
        SIGN  = 2
        DIGIT = 3
        DOT = 4
        EXPONENT = 5
        transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
                         [-1,  8, -1,  1,  4,  5],    #1 input is digits 
                         [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
                         [-1, -1, -1,  1,  2, -1],    #3 sign 
                         [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
                         [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input spi


        state = 0; i = 0
        while i < len(s):
            inputType = INVALID
            if s[i] == ' ': inputType = SPACE
            elif s[i] == '-' or s[i] == '+': inputType = SIGN
            elif s[i] in '0123456789': inputType = DIGIT
            elif s[i] == '.' : inputType = DOT
            elif s[i] == 'e' or s[i] == 'E': inputType = EXPONENT
            state = transitionTable[state][inputType]
            if state == -1: return False
            else: i += 1
        return state in (1, 4, 7, 8)
    
    def dummyWorkingCheatingApproach(self, s):
        try:
            if abs(float(s)) == float('inf'):
                return True
            if str(abs(int(float(s)))).isdigit():
                return True
        except:
            return False


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isNumber('3E10')
