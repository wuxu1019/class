'''

Definition of Tweet:
answer:
http://www.jiuzhang.com/solution/mini-twitter/#tag-highlight-lang-python
'''
import time
class Tweet:
    def __init__(self, user_id, tweet_text):
         self.user_id = user_id
         self.tweet_text = tweet_text
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
         return cls(user_id, tweet_text)


class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.rlt = {}
        self.msg = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        self.follow(user_id, user_id)
        time1 = time.time()
        self.msg[user_id].append((time1, Tweet.create(user_id, tweet_text)))
    
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        if not user_id in self.rlt:
            return []
        fol = self.rlt[user_id]
        msgl = []
        for i in fol:
            msgl.extend(self.msg[i])
        candi = sorted(msgl, reverse=1)[:10]
        return [x[1].user_id for x in candi]
        
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if not user_id in self.rlt:
            return []
        candi = sorted(self.msg[user_id], reverse=1)[:10]
        return [x[1].user_id for x in candi]


    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        self.rlt.setdefault(from_user_id, set([from_user_id]))
        self.rlt.setdefault(from_user_id, set([to_user_id]))
        self.msg.setdefault(from_user_id, [])
        self.msg.setdefault(to_user_id, [])
        self.rlt[from_user_id].add(to_user_id)
        
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        self.rlt[from_user_id].remove(to_user_id)

if __name__ == '__main__':

    s = MiniTwitter()
    s.postTweet(1, "LintCode is Good!!!")
    print s.getNewsFeed(1)
    print s.getTimeline(1)
    s.follow(2, 1)
    print s.getNewsFeed(2)
    s.postTweet(1, "LintCode is best!!!")
    print s.getNewsFeed(2)
    s.unfollow(2, 1)
    print s.getNewsFeed(2)

