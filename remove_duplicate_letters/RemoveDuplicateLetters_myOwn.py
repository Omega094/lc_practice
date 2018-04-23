class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        ctr = Counter(s)
        stack = []
        added = set()
        for i, c in enumerate(s):
            if c not in added:
                while stack and stack[-1] > c and ctr[stack[-1]] > 0:
                    added.remove(stack.pop())
                stack.append(c)
                added.add(c)
            ctr[c] -= 1
        return "".join(stack)
        
