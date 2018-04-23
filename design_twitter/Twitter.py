class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections 
        self.userIDToTweet = collections.defaultdict(collections.deque)
        self.followerToFollowee = collections.defaultdict(set)
        self.tweetCount = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetCount += 1
        self.userIDToTweet[userId].appendleft((self.tweetCount, tweetId))
        while len(self.userIDToTweet[userId]) > 10:
            self.userIDToTweet[userId].pop()
        return
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        usersToGet = list(self.followerToFollowee[userId]) + [userId]
        tweets = []
        for id in usersToGet:
            for tweetsTuple in list(self.userIDToTweet[id]):
                if len(tweets) < 10 :
                    heapq.heappush(tweets,tweetsTuple)
                    continue
                if tweetsTuple[0] > tweets[0][0]:
                    heapq.heappush(tweets,tweetsTuple)
                    heapq.heappop(tweets)
        tweets.sort(key = lambda x : -x[0])
        return [tweets[i][1] for i in xrange(0, min(10, len(tweets)))]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId and followeeId not in self.followerToFollowee[followerId]:
            self.followerToFollowee[followerId].add(followeeId)
            return
        pass

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followerToFollowee[followerId]:
            self.followerToFollowee[followerId].remove(followeeId)
            return
        pass
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
