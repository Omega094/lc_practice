class Solution(object):

    def threeSumClosest(self, num, target):
        num.sort()
        mindiff=100000
        res=0
        for i in range(len(num)):
            left=i+1; right=len(num)-1
            while left<right:
                sum=num[i]+num[left]+num[right]
                diff=abs(sum-target)
                if diff<mindiff: mindiff=diff; res=sum
                if sum==target: return sum
                elif sum<target: left+=1
                else: right-=1
        return res



#test
if __name__ == "__main__":
    sol = Solution()
    print sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
    #print sol.threeSumClosest([-1,2,1,-4], 1)
