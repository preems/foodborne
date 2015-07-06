__author__="Preetham MS"

import tweepy  # Twitter libray for python
import thread,time
from config import *
import re

class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self,api):
        self.api=api
        self.f=open('tweets.txt','w')

    def on_status(self, status):
        print status.text.encode('utf8','ignore').replace("\n"," ")
        self.f=open('tweets.txt','w')
        self.f.write( status.text.encode('utf8','ignore').replace("\n"," ")+"\n")
        self.f.close()

    def on_error(self, status_code):
    	print "error:",status_code

if __name__=="__main__":
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	tweetStreamListener = TwitterStreamListener(api)
	sampleStream = tweepy.Stream(auth = api.auth, listener=tweetStreamListener)
	sampleStream.filter(track=['food poison','food poisoning'],async=True,languages=["en"])