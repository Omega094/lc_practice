class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        counter1 = Counter(s)
        flag = False
        for i in counter1.values():
            if i%2 == 1:
                if  flag : return False
                else:
                    flag = True
        return True

    def canPermutePalindrome_simple(self, s):
        from collections import Counter
        return sum( i%2 for i in Counter(s).values()) < 2

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.canPermutePalindrome("code")
    print sol.canPermutePalindrome("carerac")

