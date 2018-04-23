#It is actually easier than I thought. 
#Only need to find the first additive sequence, 
#Then just checks along all the way to end. (With the while loop.
#If find a invalid, just break. 

class Solution(object):
    def isAdditiveNumber(self, num):
        #Length has to be more than 2
        if not num or len(num) < 3:
            return False
        length = len(num)
        for i in range(1, length):
            if i > 1 and num[0] == '0' :
                break
            for j in range(i+1, length):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second + 1:
                    break
                while third < length:
                    result = str(int(num[first:second]) + int(num[second:third]))
                    #Cool method we can have in python 
                    if num[third:].startswith(result):
                        first, second, third = second, third, third + len(result)
                    else:
                        break
                if third == length:
                    return True
        return False

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isAdditiveNumber("112358")
