class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers

    #Transpose and then reverse each row. 

    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print matrix, "after transpose"
        for i in range(n):
            matrix[i].reverse()
        return matrix



#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.rotate([[1,2],[3,4]])
