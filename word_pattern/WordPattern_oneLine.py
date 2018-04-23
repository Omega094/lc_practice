class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return map(pattern.find, pattern) == map(s.split().index, s.split())
