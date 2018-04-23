class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums: return []
        result = []
        leftVal = rightVal  = nums[0]
        counter = 1
        while counter < len(nums):
            if nums[counter] == rightVal + 1:
                rightVal = nums[counter]
                counter += 1
                continue
            else:
                result.append((leftVal, rightVal))
                leftVal = rightVal = nums[counter]
                counter += 1
        result.append((leftVal, rightVal))
        answer = []
        for pair in result:
            if pair[0] == pair[1]:
                answer.append(str(pair[0]))
            else:
                answer.append(str(pair[0]) + "->" + str(pair[1]))
        return answer


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.summaryRanges([0,1,2,4,5,7])
        

