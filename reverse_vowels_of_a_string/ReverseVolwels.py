class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #O(n) in place 
        #s = s.strip()
        if not s.strip() : return s
        vowels = set(list("aeiouAEIOU"))
        start = 0
        end = len(s)-1
        s = list(s)
        while start <= end:
            #print s
            while  start < end  and s[start] not in vowels:
                start += 1
            while  end > start and s[end] not in vowels:
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.reverseVowels('hello')
