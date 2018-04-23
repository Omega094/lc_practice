#Steps 
#1 Find the first descending point from the end. EG: 12543  -> "2543"
#2 Sort "543" -> 345.
#3 swap 2 with 3.  -> "2543" -> 3245.
#4 sort 245: -> 245. 
class Solution(object):
 
    def nextPermutation(self, nums):
        if not nums : return
        for i in range (len(nums)-1, -1, -1):
            if i -1 >= 0 and nums[i] > nums[i - 1]:
                temp = nums[i:]; temp.sort()
                for j in range(0, len(temp)):
                    if temp[j] > nums[i-1]:
                        temp[j], nums[i-1] = nums[i-1], temp[j]
                        break
                temp = sorted(temp)
                nums[i:] = temp
                break
            if i == 0: nums.reverse()
        return

#test 
if __name__ == "__main__":
    listNum = [1,3,2]
    listNum1 = [3,2,1]
    sol = Solution()
    sol.nextPermutation(listNum)
    sol.nextPermutation(listNum1)
    print listNum
    print listNum1

            
