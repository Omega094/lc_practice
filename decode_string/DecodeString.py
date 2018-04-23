class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        k = 1
        chars = defaultdict(str)
        digits = defaultdict(int)
        for c in s:
            print chars
            print digits
            if c.isdigit():
                digits[k] = digits[k]*10 + int(c)
            elif c == "[":
                k += 1
            elif c == "]":
                chars[k-1] += chars[k]*digits[k-1]
                digits[k-1] = 0
                chars[k] = ""
                k -= 1
            else:
                chars[k] += c
        return chars[1]
#test
sol = Solution()
print sol.decodeString("2[abc]3[cd]ef")

                

