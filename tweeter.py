#!/usr/bin/env python
import sys
from twython import Twython, TwythonError
import creds
import mesgs
import random


tweetStr = random.choice(open('mesgs.py').readlines())

apiKey = ['consumer_key']
apiSecret = ['consumer_token']
accessToken = ['access_token']
accessTokenSecret = ['access_token_secret']

print(apiKey)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print("Tweeted: " + tweetStr)
