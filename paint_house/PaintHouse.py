class Solution(object):
 
    #prev is the current min cost if the current house 
    # is painted by each of these three colors. 

    def minCost(self, costs):
        prev = [0] * 3
        for now in costs:
            #Paint current one with current color
            temp = prev[:]
            for i in range(0, 3):
                #Exclude the current color. 
                prev[i] = now[i] + min(temp[:i] + temp[i+1:])
        return min(prev)

