class Solution(object):
    def binarySearch(self, nums, target):
        if not nums: return -1
        start = 0
        end = len(nums) - 1
        while start <= end: 
            mid = (start + end) /2
            if nums[mid] == target: return mid
            if start == end : break
            elif nums[mid] > target: end = mid 
            else: start = mid+1
        return -1
    
    def searchInRotated(self, nums, target):
        if not nums: return -1
        if len(nums) == 1 and nums[0] == target: return 0
        start = 0
        end = len(nums) -1
        endVal = nums[-1]
        startVal = nums[0]
        while start <= end:
            mid = (start + end) /2
            if nums[mid] == target : return mid
            if start == end: break
            if target > endVal:
                if nums[mid] > target:
                    end = mid
                else:
                    if nums[mid] < startVal:
                        end  = mid
                    else:
                        start = mid + 1
            else:
                if nums[mid] < target:
                    start  = mid + 1
                else:
                    if nums[mid] > endVal:
                        start = mid + 1
                    else:
                        end = mid
        return -1    


#test 
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    nums2 = [4 ,5 ,6 ,7 ,0 ,1 ,2]
    sol = Solution()
    #print sol.binarySearch(nums, -1)
    #print sol.searchInRotated(nums2, 6)
    #print sol.searchInRotated([1],1)
    print sol.searchInRotated([1,3],3)
