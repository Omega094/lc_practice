
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
 
            token = tokens.pop(0)
           
            if token in "+-*/":
                num2 = stack.pop()
                result = stack.pop()
                operation = token
                if operation == "+":
                    result = result + num2
                elif operation == "-":
                    result = result - num2
                elif operation == "*":
                    result = result * num2
                elif operation == "/":
                    if result*num2< 0:
                        result = -((-result)/num2)
                    else:
                        result = result / num2
                stack.append(result)
            else:
                stack.append(int(token))
    
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
