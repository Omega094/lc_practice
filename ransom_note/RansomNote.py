class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for c in c1.keys():
            if c2[c] < c1[c]:
                return False
        return True
