def binary_search(arr, target):
    arr.sort()
    start = 0
    end = len(arr) -1 
    mid = (start + end) / 2
    while start <= end:
        if arr[mid] == target:
            return mid
        if start == end:
            return -1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) / 2
    return -1

#test:
if __name__ == "__main__":
    arr1 = []
    print binary_search(arr1, 9)
    arr1 = [1,2,3,4,5]
    print binary_search(arr1, 9)
    print binary_search(arr1, 3)
