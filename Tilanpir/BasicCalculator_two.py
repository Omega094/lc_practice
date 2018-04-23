class Solution(object):

    def calculate(self, s):
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
        import operator
        op = {"+":operator.add, "-":operator.sub, "*":operator.mul,"/":operator.div }
        expression = temp
        result = 0
        index = 0
        currentNum = 0
        func = op["+"]
        while index < len(expression):
            e = expression[index]
            if e in "+-":
                #evaluate the previous one
                total = func(total, d)
                #Record the current one
                func = op[e]
            elif e in "*/":
                index += 1
                d = op[e](d, int(expression[index]))
            else:
                d = int(e)
            index += 1
        return func(total, d)






