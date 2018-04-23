class Solution(object):

    def grayCodeHelper(self, n):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0','1']
        else:
            result = self.grayCodeHelper(n-1)
            newResult = []
            for code in (result):
                newBinaryString = '0'+code
                newResult.append(newBinaryString)

            for code in reversed(result):
                newBinaryString = '1'+code
                newResult.append(newBinaryString)
            return newResult

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resultStrings = self.grayCodeHelper(n)
        resultNumerical = []
        for code in resultStrings:
#                print "{0:b}".format(code)
            newCode = int(code, 2)
            resultNumerical.append(newCode)
        return resultNumerical


    def grayCode_bit(self, n):
        if not n:
            return [0]
        res = [0,1]
        #There are n bits when input is n.
        for i in range(2, n+1):
            for j in range(len(res) - 1, -1, -1):
                #"01" | with 100 ..... 
                res.append(res[j] | 1 << (i-1))
        return res


#test:
if __name__ == "__main__":
    sol = Solution()
#    print sol.grayCode(2)
    print sol.grayCode(3)
    print sol.grayCode_bit(3)
