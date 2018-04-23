class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = 0
        from collections import defaultdict
        self.userToFollowee = defaultdict(set)
        self.userToTweet = defaultdict(list)
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.userToTweet[userId].append((self.counter, tweetId))
        self.counter += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        result = []
        for id in (list(self.userToFollowee[userId]) + [userId]):
            for tweet in self.userToTweet[id]:
                if len(result) < 10 or tweet[0] > result[0][0]:
                    heapq.heappush(result, tweet)
                while len(result) > 10:
                    heapq.heappop(result)
        result.sort(reverse = True)
        return map(lambda x: x[1] , result)
                
                

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId: return 
        self.userToFollowee[followerId].add(followeeId)
 

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.userToFollowee[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
