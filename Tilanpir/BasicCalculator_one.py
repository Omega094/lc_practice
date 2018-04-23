class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result = 0
        index = 0
        sign = [1, 1]
        while index < len(s):
            if s[index].isdigit():
                number = ""
                while index < len(s) and s[index].isdigit():
                    number += s[index]
                    index += 1
                #Most critical step
                #need to pop !
                result += sign.pop()*int(number)
                #print result , sign
                continue
            if s[index] in '-+(':
                if s[index] == '-':
                    sign.append(sign[-1]*(-1))
                elif s[index] == '+':
                    sign.append(sign[-1]*1)
                else:
                    sign.append(sign[-1]*1)
            elif s[index] ==')':
                sign.pop()
            index += 1
        return result

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.calculate("(1+(4+5+2)-3)+(6+8)")


