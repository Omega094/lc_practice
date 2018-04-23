class Solution(object):
    def validWordSquare(self, strList):
        """
        :type words: List[str]
        :rtype: bool
        """
        squareLen = len(strList)
        for i in xrange(len(strList)):
            colWord = "".join([s[i]  if i < len(s) else "" for s in strList])
            if colWord != strList[i] : return False
        return True
