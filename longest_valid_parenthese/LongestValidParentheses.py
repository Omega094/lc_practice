#Key point:
# table[i] saves the length of max valid parenthese length only when parens[i-1] is ")"
# we don't care table[i] when paren[i-1] is '('
#The stack saves the index., so we can calculate the max valid paren length. 
#Look at one position back to accumulate the length when each time we pop stack and update dp[i]

class Solution(object):

    def longestValidParentheses(self, parens):
        stack = []
        maxLen = 0
        dp = [0 for i in range(len(parens)+1)]
        for i in range (0, len(parens)):
            if parens[i] == '(':
                stack.append(i)
            else:
                if stack:
                    leftParenIndex = stack.pop()
                    dp[i+1] = dp[leftParenIndex] + i - leftParenIndex + 1
        return max(dp)
    
    def longestValidParentheses_twoPass(self, parens):
        maxLen = 0
        start = -1 
        depth = 0
        for i in range(0, len(parens)):
            if parens[i] == '(':
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = i; depth = 0
                elif depth == 0:
                    maxLen = max(maxLen, i - start )
        start = len(parens); depth = 0
        for i in range (len(parens) - 1, -1, -1):
            if parens[i] == ')':
                depth += 1
            else:
                depth -= 1 
                if depth < 0:
                    start = i; depth = 0
                elif depth == 0:
                    maxLen = max(maxLen, start - i )
        return maxLen


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.longestValidParentheses("()()") == sol.longestValidParentheses_twoPass("()()")
    print sol.longestValidParentheses("()()()()()()())") == sol.longestValidParentheses_twoPass("()()()()()()())")
    print sol.longestValidParentheses("(()") == sol.longestValidParentheses_twoPass("(()")
    print sol.longestValidParentheses("(((((()((((((((((()(((((((((()") == sol.longestValidParentheses_twoPass("(((((()((((((((((()(((((((((()")


    print sol.longestValidParentheses("()()") 
    print sol.longestValidParentheses("()()()()()()())")
    print sol.longestValidParentheses("(()") 
    print sol.longestValidParentheses("(((((()((((((((((()(((((((((()")

