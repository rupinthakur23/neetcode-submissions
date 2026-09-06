class Twitter:

    def __init__(self):
        self.tweetsMap = defaultdict(list)
        self.followersMap = defaultdict(set)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        self.followersMap[userId].add(userId)

        for followeeId in self.followersMap[userId]:
            if self.tweetsMap[followeeId]:
                index = len(self.tweetsMap[followeeId]) - 1
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(heap, [time,tweetId, index - 1, followeeId])
        
        while heap and len(result) < 10:
            time,tweetId, index, followeeId = heapq.heappop(heap)
            result.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(heap, [time,tweetId, index - 1, followeeId])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followersMap[followerId]:
            self.followersMap[followerId].remove(followeeId)

        
