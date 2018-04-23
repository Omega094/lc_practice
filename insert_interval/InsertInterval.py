class Solution(object):
    def insert(self, intervals, newInterval):
        #first need to do a binary search
        if len(intervals) == 0: return [newInterval]
        start = 0
        end = len(intervals) - 1
        mid = (start + end) / 2
        while start <= end:
            mid = (start + end) / 2
            if start == end: break
            if intervals[mid][0] > newInterval[0]:
                end = mid
            else:
                start = mid + 1
        if newInterval[0] <= intervals[start][0]: 
            mid = start
        else:
            mid = start + 1
        intervals.insert(mid, newInterval)
        #Starting from here we can actually copy merge interval. 
        #Solution below has less time cost but delete item from 
        #list might be expensive. 
        if mid > 0 and intervals[mid][0] <= intervals[mid-1][1]:
            if intervals[mid-1][1] <= intervals[mid][1]:
                intervals[mid-1][1] = intervals[mid][1]
            del intervals[mid]
            mid = mid - 1
        while mid < len(intervals) - 1 and intervals[mid][1] >= intervals[mid+1][0]:
            if intervals[mid][1] <= intervals[mid+1][1]:
                intervals[mid][1] = intervals[mid+1][1]
            del intervals[mid+1]
        return intervals

#Find two boundries, left and right . 


    def insert_better(self, intervals, newInterval):
        start = newInterval[0]
        end = newInterval[1]
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right][1]:
                if end < intervals[right][0]:
                    break
                start = min(start, intervals[right][0])
                end = max(end, intervals[right][1])
            else:
                left+=1
            right += 1
        return intervals[:left] + [ [start, end]] + intervals[right:]


#test 
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,9]
    print sol.insert(intervals, newInterval)
    print sol.insert_better(intervals, newInterval)
    intervals2 = []
    print sol.insert(intervals2, newInterval)
    intervals3 = [[1,5]]
    newInterval3 = [2,3]
    print sol.insert(intervals3, newInterval3)
