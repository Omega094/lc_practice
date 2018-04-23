class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    def getSum_2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0 : return a
        if a == 0: return n
        return self.getSum(a^b, a&b << 1)

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.getSum_2(-1, 2)
