class Solution(object):

    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        expr = list(expression)
        while len(stack) > 1 or expr:
            tail = stack[:5]
            if len(tail) == 5 and tail[1] == '?' and tail[3] == ':':
                tail = tail[2] if tail[0] == 'T' else tail[4]
                stack =  [tail] + stack[5:]
            else:
                stack.insert(0,expr.pop())
        return stack[0] if stack else None
            
