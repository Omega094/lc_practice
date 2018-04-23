def partition(arr, start, end):
    piviot = start 
    if start >= end : return 
    for i in xrange(start, end ):
        if arr[i] < arr[piviot]:
            arr[i], arr[piviot] = arr[piviot], arr[i]
            piviot += 1
    partition(arr, start, piviot)
    partition(arr, piviot+1, end)
    return

def quickSort(arr):
    partition(arr, 0, len(arr))

#test
a = [7,2,4,8,9,1,0,5]
quickSort(a)
print a


        
