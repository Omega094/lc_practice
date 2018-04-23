class Solution(object):

    def nextPermutation(self, nums):
        if not nums: return 
        for i in range( len(nums)-1, -1, -1):
            #Find the point from the end where
            #descending starts 
            if i-1 >= 0 and nums[i] > nums[i-1]:
                temp = nums[i:]
                temp.sort()
                #Find the smallest one in temp 
                #That is larger than num[i-1]
                for j in range(0, len(temp)):
                    if temp[j] > nums[i-1]:
                        temp[j], nums[i-1] = nums[i-1], temp[j]
                        break
                #need to sort temp
                temp.sort()
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
