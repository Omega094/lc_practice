class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return len(set(zip(pattern, str.split()))) == len(set(pattern)) == len(set(str.split())) and len(str.split()) == len(pattern)
