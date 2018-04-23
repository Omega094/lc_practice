class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negativeFlag = (numerator*denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        #The list we put all digits into
        numList = []
        dictForLoop = {}
        digitCounter = 0
        recurringPart = None 
        while True:
            currentDigit = numerator / denominator
            currentRemainder = numerator % denominator
            numerator = currentRemainder*10 
            numList.append(str(currentDigit))
            digitCounter += 1
            if numerator == 0:
                break
            if digitCounter >= 1:
                #print dictForLoop
                firstAppear = dictForLoop.get(currentRemainder, None)
                #print firstAppear
                if not firstAppear:
                    dictForLoop[currentRemainder] = digitCounter
                else:
                        recurringPart = numList[firstAppear:digitCounter]
                        numList = numList[:firstAppear]
                        break
        if not numList: return "0"
        beforeDot = numList[0]
        result = beforeDot
        if numList[1:] or recurringPart:
            result += '.'+"".join(numList[1:])
        if recurringPart:
            result += "(" + "".join(recurringPart) + ")"
        if negativeFlag:
            result = "-" + result
        return result
 

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.fractionToDecimal(1, 5)
    print sol.fractionToDecimal(1, 17)
