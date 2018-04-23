class Solution(object):

    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        length = len(s1)
        length2 = len(s2)
        if length!=length2: return False
        if s1 == s2: return True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2: return False
        for i in range (1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) : return True
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]): return True
        return False




#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.isScramble("great", "rgtae")
