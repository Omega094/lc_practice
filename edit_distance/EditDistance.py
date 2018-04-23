class Solution(object):
    def minDistance(self, word1, word2):
        #Dynamic Programming
        #First index is for empty string. 
        table = [[0 for j in range(0, len(word2) + 1)] for i in range(0, len(word1)+1)]
        #Note here is i
        for i in range (0, len(word1)+ 1):
            table[i][0] = i
        #note here is j
        for j in range (0, len(word2)+ 1):
            table[0][j] = j
        for i in range (1, len(word1)+1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] != word2[j-1]:
                    #Take the min , plus one
                    table[i][j] = min(table[i][j-1], table[i-1][j], table[i-1][j-1])+1
                else:
                    #This one needs to be careful.
                    table[i][j] = min(table[i][j-1]+1, table[i-1][j]+1, table[i-1][j-1])
        return table[len(word1)][len(word2)]
                        




#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.minDistance("fdfd","fdfdfdfdf")
