class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        #Count bulls:
        from collections import Counter
        setS = Counter(secret)
        setCow = set()
        for i in xrange(0, len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                setS[secret[i]] -= 1
        for i in xrange(0, len(guess)):
            if secret[i] != guess[i] and guess[i] in setS and setS[guess[i]] > 0:
                    cow += 1
                    setS[guess[i]] -= 1
        return str(bull)+"A"+str(cow)+"B"
    
    def getHint_simple(self, secret, guess):
        import operator
        bull = sum(map(operator.eq, secret, guess))
        bullAndCow = sum(min(secret.count(c), guess.count(c)) for c in "0123456789")
        return '%dA%dB' % (bull, bullAndCow - bull)


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.getHint("1123", "0111")
    print sol.getHint_simple("1123", "0111")
