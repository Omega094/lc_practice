class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need, missing = collections.Counter(p), len(p)
        start = 0; result = []; length = len(p)
        for end, c in enumerate(s):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing :
                while start < end and need[s[start]] < 0 :
                    need[s[start]] += 1
                    start += 1
                if end - start + 1 == length:
                    result.append(start)
        return result 
        
                
        

