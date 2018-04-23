class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        if n - p.count('*') > m:   #avoid TLE
            return False
        table = [ [False for _ in xrange(len(s) + 1)] for _ in xrange(len(p)+1)]
        table[0][0] = True
        for i in xrange(1, len(p) +1):
            if p[i-1] == "*": table[i][0] = table[i-1][0]
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] == "*":
                    table[j][i] = table[j][i-1] or table[j-1][i] or table[j-1][i-1]
                elif p[j-1] == "?":
                    table[j][i] = table[j-1][i-1]
                else:
                    if p[j-1] == s[i-1]:
                        table[j][i] = table[j-1][i-1]
        return table[len(p)][len(s)]
