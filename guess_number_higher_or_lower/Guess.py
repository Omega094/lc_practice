# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = (start + end) // 2
        while start != end:
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return start
