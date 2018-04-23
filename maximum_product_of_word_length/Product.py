#The idea is to use a bitmask to save what char is in the word. 
#given that the input is only alphabetical , 
#We should come up with this solution natually. 

class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        bitMask = [0]*length
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                bitMask[i] |= 1 << (ord(c) - ord('a'))
        
        ans = 0
        for i in xrange(0, length):
            for j in xrange(i+1, length):
                if bitMask[i] & bitMask[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
