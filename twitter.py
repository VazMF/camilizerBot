import tweepy
import time

auth = tweepy.OAuthHandler('AItBFwiBkmpZjmYtNkBV3aUB7', '1SYsrHr8VO8UoYMAVkBSRvORfH36YYsRF82PKPiL1vlAhlGCHA')
auth.set_access_token('1318379731566329856-vxipAFosb3PZtqE3CthIzfusEGkzGm', 'Kijtxa5zRXqSjSiDIvSxD61BtkJY2u2QJRENqGH9LuPO6')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'camila cabello perfeita'
numTweets = 200

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print('tweet retweetado e favoritado')
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
