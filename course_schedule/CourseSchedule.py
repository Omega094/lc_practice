class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        childsForEachNode = [[] for i in range(numCourses)]
        for pair in prerequisites:
            targetCourseNode = pair[0]
            prerequeCourseNode = pair[1]
            degrees[targetCourseNode] += 1
            childsForEachNode[prerequeCourseNode].append(targetCourseNode)
        print childsForEachNode
        flag = True
        courses = set(range(numCourses))
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in childsForEachNode[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)
        return len(courses) == 0

    def canFinish_fast(self, numCourses, prerequisites):
        from collections import deque
        prerequeToTarget = [[] for _ in xrange(numCourses)]
        targetCourseDegree = [0] * numCourses
        for pair in prerequisites:
            prerequisites = pair[1]
            targetCourse = pair[0]
            targetCourseDegree[targetCourse] += 1
            prerequeToTarget[prerequisites].append(targetCourse)
        dQueue = deque()
        for i in range (numCourses):
            if targetCourseDegree[i] == 0:
                dQueue.append(i)
        k = 0
        while dQueue:
            feasibleCourse = dQueue.popleft()
            k += 1
            for targetCourse in prerequeToTarget[feasibleCourse]:
                targetCourseDegree[targetCourse] -= 1
                if targetCourseDegree[targetCourse] == 0:
                    dQueue.append(targetCourse)
        return k == numCourses 


#test:
if __name__ == "__main__":
    courseNum = 10
    courses = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
    sol = Solution()
    print sol.canFinish(courseNum, courses)
    print sol.canFinish_fast(courseNum, courses)
