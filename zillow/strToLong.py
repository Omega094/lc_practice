# Complete the function below.

def parse_long(s):
    if type(s) != str:
        raise TypeError("Input type should be string.")
    if "." in s:
        raise ValueError("Input should not be factorial.")
    negativeFlag = False
    if s[0] == "-":
        negativeFlag = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    result = 0
    for c in s:
        if c.isalpha():
            raise ValueError("Input is not valid.")
        diff = ord(c) - ord("0")
        result = result*10 + diff
    #Assume our system is 32 bits. (Although in python it handles overflow)
    if (result > 2147483647 and not negativeFlag) or (result > 2147483648 and negativeFlag):
        raise ValueError("The value overflows.")
    if negativeFlag:
        return result*(-1)
    return result

print parse_long("1234E")
