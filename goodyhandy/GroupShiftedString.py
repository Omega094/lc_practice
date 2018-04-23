class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        wordDict = defaultdict(list)
        for s in strings:
            result = []
            for c in s:
                result.append((ord(c) - ord(s[0])) % 26)
            wordDict[tuple(result)].append(s)
        out = []
        for val in wordDict.values():
            out.append(val)
        return out
