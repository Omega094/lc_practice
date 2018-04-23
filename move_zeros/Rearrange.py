def rearrange(arr):
    prev = 0
    for i, n in enumerate(arr):
        if arr[i] <  0:
            arr[i], arr[prev] = arr[prev], arr[i]
            prev += 1
    return arr

#test:
print rearrange([-2,-1,2,1,2,-14,4])
