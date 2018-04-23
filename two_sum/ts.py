def findTs(lst, target):
    result = []
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j] == target:
                result.append((lst[i], lst[j]))
    return result

def findTs2(lst, target):
    result = []
    d = set()  
    for i in range(0, len(lst)):
        if target-lst[i] in d:
            result.append((lst[i], target-lst[i]))
        d.add(lst[i])
    return result


a = [2,1,3,7,5]
t = 8


print findTs(a, t)
print findTs2(a, t)


