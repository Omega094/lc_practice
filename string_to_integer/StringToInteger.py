class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        if not str:
            return 0
        else:
            is_negative = False
            if str[0] == '-':
                is_negative = True
                str = str[1:]
            elif str[0] == '+':
                str = str[1:]
            result = 0
            for c in str:
                if not c.isdigit(): break
                diff = ord(c) - ord('0')
                result = 10*result + diff
            if result > 2147483647 and not is_negative: result = 2147483647
            if result > 2147483648 and is_negative: result = 2147483648
            if is_negative:
                return result*(-1)
            return result


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.myAtoi('-123')

