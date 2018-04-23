class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        stack = []
        left = "({["
        right = ")}]"
        pair= {"(":")","[":"]","{":"}" }
        for p in s:
            if p in left:
                stack.append(p)
            else:
                if not stack: return False
                if  pair[stack[-1]] != p: return False
                stack.pop()
        return len(stack) == 0
        
