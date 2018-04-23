#Complexity is O(2n)
#Since each index will be entered/deleted from hash table at most twice.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        positionDict = defaultdict(int)
        back = 0
        front = 0
        maxLen = 0
        while front != len(s):
            if s[front] in positionDict:
                nextPos = positionDict[s[front]] + 1
                while back != nextPos:
                    del positionDict[s[back]]
                    back += 1
            positionDict[s[front]] = front
            maxLen = max(maxLen, front - back + 1)
            front += 1
        return maxLen
        
