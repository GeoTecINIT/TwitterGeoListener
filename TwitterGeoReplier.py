import time

import TwitterPlaceProcessing as tpl
import TwitterPoster as tp
from key import TwitterKey as tapi

api = tapi.getTwitterApi()

baseTest ='I guess @%s was here at %s: '
baseTestPlace = 'I guess @%s from %s you see this at %s' 
baseTest_fail = 'I cannot guess #whereYouWere @%s try to give me a clue ... '

def replyWithLocation(tweet):
	tweet_id = tweet["id_str"]
	coordinates = tweet['coordinates'] 
	place = tweet['place']
	user_obj = tweet["user"]
	user = user_obj["screen_name"]
	status = ''
	if coordinates != None:
		location = coordinates['coordinates']
		status = baseTest % (user, time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) )
		tp.replySceneLocation(tweet_id, status, location)
	elif place != None:
		location = tpl.getPlaceCentroid(place)
		zoom = 12
		status = baseTestPlace % (user, place['full_name'], time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
		tp.replyMapLocation(tweet_id, status, location, zoom)
	else:
		status = baseTest_fail % user
		tp.replyTweet(tweet_id, status)
		print("no-location post")
		


if __name__ == "__main__":

	tweet_id = '699622396299513857'
	tweet = api.get_status(tweet_id)
	replyWithLocation(tweet)