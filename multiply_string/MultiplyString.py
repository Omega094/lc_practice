class Solution(object):

    def multiply(self, num1, num2):
        l1 = map(int, num1[::-1])
        l2 = map(int, num2[::-1])
        result = 0
        for i in range(0, len(l1)):
            for j in range(0, len(l2)):
                result += (l1[i]*l2[j]*10**(i+j))
        return str(result)

    def multiply_correct(self, num1, num2):
        res = [0]*(len(num1) + len(num2))
        l1 = map(int, num1)[::-1]
        l2 = map(int, num2)[::-1]
        for i, n1 in enumerate(l1):
            for j, n2 in enumerate(l2):
                res[i+j] += n1*n2
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))



#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.multiply("11", "11")
    print sol.multiply_correct("99","99")
