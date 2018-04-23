def findKth(arr, k):
    if len(arr) == 1: return arr[0]
    smaller = []
    larger = []
    piviot = arr[0]
    for n in arr:
        if n < piviot:
            smaller.append(n)
        if n > piviot:
            larger.append(n)
    if len(smaller) >= k :
        return findKth(smaller, k)
    if k > len(arr) - len(larger):
        return findKth(larger, k - (len(arr) - len(larger)))
    return piviot



def findMedianWithThreshold(arr, threshold):
    arr = filter(lambda x : x >= threshold)
    return findMedian(arr)

print findKth([1,2,3,4,5], 5)
