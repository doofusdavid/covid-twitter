import tweepy
import requests
import sched
import time
s = sched.scheduler(time.time, time.sleep)


def pushover_push(text):
    url = "https://api.pushover.net/1/messages.json"
    params = {"token": "aqd8yqjyuaftqixmif1kyg72832say",
              "user": "udmwmhh7k59p92bb6vdq4v7b67k5n2",
              "message": text}
    x = requests.post(url, data=params)


def search_twitter():
    print("searching")
    api_key = "XeyfKj4x8bIiE3IwaSN9vyrt0"
    api_secret = "DoIAlo0o8aEsj382azpv1RkWJC5mlUBijzuQX52qiLZniR4lUH"

    auth = tweepy.AppAuthHandler(api_key, api_secret)

    api = tweepy.API(auth)
    tweets = api.user_timeline(
        "COVaxAlerts", trim_user=True, exclude_replies=True, include_rts=False)
    locations = ["collins", "loveland", "laporte", "la porte"]
    for tweet in tweets:
        if any(x in tweet.text.lower() for x in locations):
            pushover_push(tweet.text)
    s.enter(60, 1, search_twitter, ())


s.enter(60, 1, search_twitter, ())
s.run()
