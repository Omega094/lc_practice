class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0: num += 0x100000000
        ans = []
        hexs = '0123456789abcdef'
        while num:
            ans.append(hexs[num%16])
            num /= 16
        return "".join(ans[::-1]) if ans else "0"
