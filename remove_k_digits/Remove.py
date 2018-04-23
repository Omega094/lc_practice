class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        temp = k
        for  n in  num:
            while result and result[-1] > n and temp:
                result.pop()
                temp-=1
            result.append(n)
        return ''.join(result[:-temp or None]).lstrip('0') or '0'

