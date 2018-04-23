class Solution(object):

    def plusOne(self, digits):
        carryDigit = 1
        for i in range(len(digits)-1, -1, -1):
            currentDigit = (digits[i] + carryDigit) % 10
            carry = (digits[i] + carryDigit) // 10
            digits[i] = currentDigit
        if carry:
            digits.insert(0, carry)
        return digits

#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.plusOne([9,9,9])

