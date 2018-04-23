a = [(1,2),(-1, 3), (-1, 2), (2,3), (1,-5)]
a.sort(cmp = lambda x, y : x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
print a 
