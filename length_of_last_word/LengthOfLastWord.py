class Solution(object):
    
    def lengthOfLastWord(self, s):
        s = s.strip()
        if not s: return 0
        return len(s.strip()[-1])

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLastWord(' a b ')
