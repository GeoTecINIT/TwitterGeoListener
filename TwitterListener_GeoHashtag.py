import json
import pymongo
import tweepy

import TwitterGeoReplier as gr
from key import TwitterKey as tapi
from key import MongoDBKey as mongo

api = tapi.getTwitterApi()
auth = tapi.getTwitterAuth()



class CustomStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = mongo.getDB()
        self.collection = mongo.getCollection()

    def on_data(self, tweet):
        tweet_json = json.loads(tweet)
        try:
            self.collection.insert(tweet_json)
        except Exception, e:
            print ("Error inserting data to MongoDB ")
        gr.replyWithLocation(tweet_json)

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['#TestingDP'])