class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #complexity is O(k*n)
        #k is the length of unique set 
        #greddy algorithm
        import collections
        result = ""
        for i in range(len(set(s))):
            print result, s
            top = s[0]
            topIndex = 0
            counterDict = collections.Counter(s)
            for j in xrange(len(s)):
                #Remember we still need to replace if it is equal

                if s[j] <= top:
                    top = s[j]
                    index = j
                if counterDict[s[j]] == 1:
                    break
                counterDict[s[j]] -= 1
            result += top
            s = s[index+1:].replace(top, "")
        return result

    def removeDuplicateLetters_stack(self, s):
        #complexity is O(n)
        import collections
        stack = []
        counterDict = collections.Counter(s)
        distinctSet = set()
        for i, c in enumerate(s):
            if c not in distinctSet:
                print c, stack, counterDict
                while stack and stack[-1] > c and counterDict[stack[-1]] >= 1 :
                    temp = stack.pop()
                    distinctSet.remove(temp)
                distinctSet.add(c)
                stack.append(c)
            counterDict[c] -= 1
        return "".join(stack)
    

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.removeDuplicateLetters("cbacdcbc")
    print sol.removeDuplicateLetters_stack("cbacdcbc")
