import json

import pymongo
import tweepy

import TwitterGeoReplier as gr
from key import TwitterKey as tapi

api = tapi.getTwitterApi()
auth = tapi.getTwitterAuth()



class CustomStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        #self.db = MongoClient("mongodb://%s:27019" % mdb.serverUrl)
        self.db = pymongo.MongoClient().twitter

    def on_data(self, tweet):
        tweet_json = json.loads(tweet)
        #try:
        #    self.db.timeLine.insert(tweet_json)
        #except Exception, e:
        #    print ("No Mongo Client")
        

        gr.replyWithLocation(tweet_json)


        #print ("Stored in MongoDB & replied to: @%s at %s " % (tweet['user']['screen_name'] , time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) ) )

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['#TestingDP'])