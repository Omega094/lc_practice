#Process */ first then +-
#Simpler than I thought. 
#Pass twice 
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
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
        start = 1
        result = 0
        import operator
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        from collections import deque
        temp = deque(temp)
        stack = []
        while temp:
            val = temp.popleft()
            if val in "*/":
                stack.append( str (op[val](int(stack.pop()),int( temp.popleft()))))
            else:
                stack.append( val )
        stack2 = []
        stack = deque(stack)
        while stack:
            val = stack.popleft()
            if val in "+-":
                stack2.append(op[val](stack2.pop(),int( stack.popleft())))
            else:
                stack2.append( int(val)) 
        return  stack2[0]

#test
sol = Solution()
print sol.calculate(" 3+5 / 2 ")
