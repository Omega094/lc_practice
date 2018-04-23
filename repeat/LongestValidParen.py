class Solution(object):

    def longestValidParentheses(self, parens):
        stack = []
        #Save the longest valid paren till the grid
        dp = [ 0 for i in xrange(len(parens)+1)]
        for i, paren in enumerate(parens, 1):
#            print stack
#            print paren
            if paren == "(":
                stack.append(i)
            else:
                if stack:
                    lastIndex = stack.pop()
                    dp[i] = dp[lastIndex-1] + i - lastIndex + 1
#                    print dp , "This is dp"
                else:
                    dp[i] = 0
        return max(dp)


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.longestValidParentheses("()()") 
    print sol.longestValidParentheses("()()()()()()())")
    print sol.longestValidParentheses("(()") 
    print sol.longestValidParentheses("(((((()((((((((((()(((((((((()")


