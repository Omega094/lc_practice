class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        #The idea is greedy. 
        #We can have a variable called known_sum
        #There are two scenarios 
        #1: nums[i] <= known_sum and i < len(nums), we increment i and known_sum can 
        # be incremented by nums[i]
        #2: known_sum < nums[i], in this case, we double known sum and increment the counter.  
        
        known_sum = 1
        count = 0
        i = 0
        while known_sum <= n :
            if i < len(nums) and nums[i] <= known_sum:
                #In this case 
                #known_sum covers [1, known_sum + nums[i]]
                #Because:
                #Since known_sum >= nums[i]
                #Therefore any point between 1 to nums[i] could be covered by [1..nums[i-1]]
                #When we add nums[i] in to it, 
                #Anypoint from [known_sum , known_sum + nums[i]] is just
                #known_sum + nums[i] SUBTRACT the combination that forms any value from 1 to nums[i]  
                known_sum += nums[i] 
                i += 1
            else:
                known_sum *= 2
                count += 1
        return count

#Test
if __name__ == "__main__":
    sol = Solution()
    print sol.minPatches([1, 5, 10], 20)
