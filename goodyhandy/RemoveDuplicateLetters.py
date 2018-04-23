class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cCounter = Counter(s)
        stack = []
        uniqueSet = set()
        for i, c in enumerate(s):
            while stack and cCounter[stack[-1]] > 0 and c < stack[-1] and c not in uniqueSet :
                uniqueSet.remove(stack.pop())
            if c not in uniqueSet:
                stack.append(c)
                uniqueSet.add(c)
            cCounter[c] -= 1
        return "".join(stack)

#test
sol = Solution()
print sol.removeDuplicateLetters("abacb")
