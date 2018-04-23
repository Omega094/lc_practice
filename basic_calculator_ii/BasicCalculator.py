class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import operator
        temp = []
        currentNum = ""
        for c in s:
            if c not in "+-*/":
                currentNum += c
            else:
                temp.append(currentNum)
                temp.append(c)
                currentNum = ""
        temp.append(currentNum)
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        expression = temp
        total = 0
        d = 0 # The most recent number 
        index = 0
        func = op['+']
        while index < len(expression):
            e = expression[index]
            if e in '+-':
                #Evaluate the previous one
                total = func(total, d)
                #Record the current one
                func = op[e]
            #Move one index forward to evluate result, save it in d
            elif e in '*/':
                index += 1
                d = op[e](d, int(expression[index]))
            else:
                d = int(e)
            index += 1
        return func(total, d)

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.calculate("3+2*22")
