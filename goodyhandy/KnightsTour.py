N = 5
visited = [[False for x in range(N)] for y in range(N)]

def move(x, y, m):
    result = False
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] == True:
        return False
    visited[x][y] = True
    if m == (N*N-1) :
        print "solution Found"
        return True
    else:
        print x, ",", y
        if (move(x+2,y+1,m+1) or move(x+2,y-1, m+1)
                or move(x-2,y+1,m+1) or move(x-2,y-1,m+1)
                or move(x+1,y-2,m+1) or move(x+1,y+2,m+1)
                or move(x-1,y-2,m+1) or move(x-1,y+2,m+1)):
            print x,",",y
            return True
    visited[x][y] = False
    return False
print move(2,1,0)
