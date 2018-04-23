class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in xrange(len(digits)-1, -1, -1):
            s  = digits[i] + carry
            digits[i] = s%10
            carry = s/10
        if carry == 1:
            digits.insert(0, 1)
        return digits
