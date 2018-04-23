def solution(A, D):
    # write your code in Python 2.7
    #If single jump can cross the river.
    if D > len(A) : return 0;
    #handle invalid inputs.  
    if not A or len(A) == 0 or D == 0: return -1
    #Use a table to save the min time that we need to jump to the ith stone. 
    table = A[:] 
    for i in xrange(D, len(A)):
        if A[i] != -1:
            #Look backward D steps to find the earlist stone to jump from. 
            timeToCurrent = float('inf')
            for j in range(1, D+1):
                if table[i-j] == -1:
                    continue
                timeToCurrent = min(timeToCurrent, table[i-j])
            #The earlist time to jump to current stone is 
            #the max time between 
            #1: The earlist time to jump to a stone that locates D steps back
            #2: The time current stone runs out of water. 
            table[i] = -1 if timeToCurrent == float('inf') else max(timeToCurrent, A[i])
    #For the time to cross, simply look backward D steps from the last stone. 
    timeToCross = float('inf')
    for j in xrange(1, D+1 ):
        if table[-j] == -1:
            continue
        timeToCross = min(timeToCross, table[-j])
    if timeToCross == float('inf') : return -1
    return timeToCross

