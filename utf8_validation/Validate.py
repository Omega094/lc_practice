class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        masks = [0x0, 0b10000000, 0b11100000, 0b11110000, 0b11111000]
        bits =  [0x0, 0b00000000, 0b11000000, 0b11100000, 0b11110000]
        while data:
            for x in (4,3,2,1,0):
                if data[0] & masks[x] == bits[x]:
                    break
            if x == 0 or len(data) < x:
                return False
            for y in range(1, x):
                if data[y] & 0b11000000 != 0b10000000:
                    return False
            data = data[x:]
        return True
