class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validParen(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0: return False
            return count == 0
        queue = [s]
        if validParen(s) : return [s]
        while queue:
            newQueue = set()
            for s in queue:
                for i in xrange(len(s)):
                    if s[i] in "()":
                        newQueue.add(s[:i]+s[i+1:])
            result = filter(validParen, newQueue)
            if result :
                return result
            queue = newQueue
        return []
