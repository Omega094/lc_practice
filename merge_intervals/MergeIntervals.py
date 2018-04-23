class Solution(object):

    def merge(self, intervals):
        intervals.sort()
        solution = []
        solution.append(intervals.pop(0))
        for interval in intervals:
            if interval[0] > solution[-1][1]:
                solution.append(interval)
            else:
                if interval[1] > solution[-1][1]:
                    solution[-1][1] = interval[1]
        return solution




#test:
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print sol.merge(intervals)

