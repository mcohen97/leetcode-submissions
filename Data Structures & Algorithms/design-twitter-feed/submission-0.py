import time

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followees = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        userTweets = self.tweets.get(userId, [])
        userTweets.append((tweetId, time.time()))
        self.tweets[userId] = userTweets
    

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followees.get(userId, set())

        followeesPosts = map(lambda item: item[1].copy(), 
        filter(lambda item: (item[0] in followees or item[0] == userId) and item[1], self.tweets.items()))

        res = []
        heap = list(map(lambda feed: (-feed[-1][1], feed),followeesPosts))
        heapq.heapify(heap)

        i = 1

        while heap and i <= 10:
            (priority, feed) = heapq.heappop(heap)
            res.append(feed.pop()[0])
            if feed:
                heapq.heappush(heap, (-feed[-1][1], feed))
            i+= 1
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.followees.get(followerId, set())
        followees.add(followeeId)
        self.followees[followerId]=followees
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followees.get(followerId, set())
        if followeeId in followees:
            followees.remove(followeeId)
        self.followees[followerId]=followees

        
