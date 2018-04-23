import heapq



class Solution(object):
    #It should be better to pass an iterator in here. 
    def topK(self, lst, k):
        topK = []
        heapq.heapify(topK)
        topK.append(lst[0])
        lst = lst[1:]
        for num in lst:
            if len(topK) < k:
                heapq.heappush(topK, num)
            else:
                if num > topK[0] :
                    heapq.heappush(topK, num)
                    while len(topK) > k:
                        heapq.heappop(topK)
        topK.sort()
        return topK

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.topK([5,6,2,3,4,1,9,0], 3)
    print sol.topK([9,0,6,2,1,10,8,2,3,1,99,4], 5)
