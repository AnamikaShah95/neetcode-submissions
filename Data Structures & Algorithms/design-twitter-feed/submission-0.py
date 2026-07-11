from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        self.followers[userId].add(userId)
        
        for user in self.followers[userId]:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                min_heap.append((time, tweetId, user, index - 1))
        
        heapq.heapify(min_heap)
        
        while min_heap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                next_time, next_tweetId = self.tweets[user][index]
                heapq.heappush(min_heap, (next_time, next_tweetId, user, index - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)