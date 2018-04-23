def numDiffs(nums):
    result = []
    result.append(nums[0])
    for i, currentNum in enumerate(nums[1:], 1):
        diff = (currentNum - nums[i-1])
        if abs(diff) <= 127:
            result.append(diff)
        else:
            result.append(-128)
            result.append(diff)
    return result

print numDiffs([25400, 26300, 2, 128, 5])
