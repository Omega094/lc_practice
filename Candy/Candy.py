def candy( ratings):
    n = len(ratings)
    Useq = [0 for i in range(n)]
    for i in xrange(1, n):
        if ratings[i]>ratings[i-1]:
            Useq[i] = Useq[i-1]+1
    print Useq
    Dseq = [0 for i in range(n)]
    for i in xrange(n-2, -1, -1):  #from i = n-2, ... 1, 0 ## will not reach -1!!
        if ratings[i]>ratings[i+1]:
            Dseq[i] = Dseq[i+1]+1

    candies = [max(Useq[i], Dseq[i])+1 for i in range(n)]
    print candies
    return sum(candies)



candy([1,2,2,2])