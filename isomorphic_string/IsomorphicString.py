class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictSToT = {}
        dictTToS = {}
        for i, c in enumerate(s):
            print dictSToT
            print dictTToS
            if c in dictSToT:
                if t[i] not in dictTToS: return False
                if not (dictSToT[c] == t[i] and dictTToS[t[i]] == c):
                    return False
            else:
                dictSToT[c] = t[i]
                if t[i] in dictTToS: return False 
                dictTToS[t[i]] = c
        return True
    
    def isIsomorphic_2(self, s, t):
        sourceMap, targetMap = {}, {}
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])
            if source is None and target is None:
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True 
    
    def isIsomorphic_3(self, s, t):
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isIsomorphic("ab","aa")
