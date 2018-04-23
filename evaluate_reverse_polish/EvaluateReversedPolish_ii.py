class Solution(object):

    def evalRPN(self, tokens):
        stack = []
        import operator
        operatorDict = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
        while tokens:
            currentToken = tokens.pop(0)
            if currentToken in "+-*/":
                num2 = stack.pop()
                result = stack.pop()
                func = operatorDict[currentToken]
                result = func(result, num2)
                stack.append(result)
            else:
                stack.append(int(currentToken))
        return stack[0]

#test
if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    sol = Solution()
    print sol.evalRPN(tokens)
    tokens2 = ["4","13","5","/","+"]
    sol = Solution()
    print sol.evalRPN(tokens2)
    tokens3 = ["4","13","5","/","+"]
    sol = Solution()
    print sol.evalRPN(tokens3)

