
#The goal is to find the first num in the list that does not satisfy
#A[i] != i + 1  (i starts from 0)
#In linear time and constant space. 
 
class Solution(object):

    def firstMissingPositive(self, A):
        length = len(A)
        for i in xrange(length):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > length or A[i] == A[A[i]-1]: break
                # swap A[i], A[A[i]-1]  
                t = A[A[i]-1]; A[A[i]-1] = A[i]; A[i] = t
                #Index changed, cannot directly swap ~              
                #A[i], A[A[i]-1] = A[A[i]-1], A[i] 
        for i in xrange(length):
            if A[i] != i + 1:
                return i + 1
        return length + 1


#test 
if __name__ == "__main__":
    sol = Solution()
    print sol.firstMissingPositive([3,4,-1,1]) 
