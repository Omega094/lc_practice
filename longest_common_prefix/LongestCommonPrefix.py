class Solution(object):
        def longestCommonPrefix(self, strings):
            if not strings: return ""
            shorteststr = min(strings)
            prefixLen = len(shorteststr)
            longestPrefix = shorteststr 
            while prefixLen > 0:
                for i, string in enumerate (strings):
                    if not string.startswith(longestPrefix[:prefixLen]):
                        break
                    if i == len(strings) - 1:
                        return longestPrefix[:prefixLen]
                prefixLen -= 1
            return longestPrefix[:prefixLen]


#test : 
if __name__ == "__main__":
    listStr = ["abcd", "abcdefg", "abcdefgijl"]
    listStr2 = ['a', 'b']
    sol = Solution()
    print sol.longestCommonPrefix(listStr)
    print sol.longestCommonPrefix(listStr2)
