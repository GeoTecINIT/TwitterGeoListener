import time
import StaticMap as sm
import StreetViewScene as gsv
from key import TwitterKey as tapi

api = tapi.getTwitterApi()

tempMap_file = 'tempMap.png'
tempSc_File = 'tempScN.png'

def postTweet(status):
    status = status + 'at ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    api.update_status(status)
    print ('Posted: ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

def replyTweet(t_id, status):
    status = status + 'at ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    api.update_status(status, t_id)
    print ('Posted: ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

def replyTweetWithMedia(file, status, t_id ):
    status = status + 'at ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    api.update_with_media(file, status, t_id)
    print ('Posted with media: ' + file + ' at: ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

def postGeoTweet(self, status, lat, lon):
    self.api.update_status()

def postMediaTweet( status, media):
    post = api.update_with_media(media,status)
    print ('Posted - file: %s' % media )

def postGeoMediaTweet(status, lat, lon, media):
    post = api.update_with_media(media,status,lat,lon)
    print ('Posted at %s,%s - file: %s' % (str(lat), str(lon), media) )
    
def getTempMap(lat,lon,zoom):
    location = [lat, lon]
    sm.getMap(tempMap_file, location, zoom)

def replyMapLocation(t_id, status, location, zoom):
    lon = location[0]
    lat = location[1]
    getTempMap(lat,lon,zoom)
    api.update_with_media(tempSc_File, status, t_id)
    print ('Posted at %s,%s - file: %s' % (str(lat), str(lon), tempMap_file) )

def replySceneLocation(t_id,status,location):
    lon = location[0]
    lat = location[1]
    location = [lat, lon]
    gsv.getScene(tempSc_File,location)
    post = api.update_with_media(tempSc_File, status, t_id)
    print ('Posted scene at %s,%s - file: %s' % (str(lat), str(lon), tempSc_File) )



if __name__ == "__main__":
    text = "hello #twitter, from #tweepy #api "
    #postTweet ( text )

    geotec_location = [39.9937928, -0.0735718]
    text = "I'am at #geotec lat/lon %s and here is my map - %s" % (str (geotec_location), time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
    getMap(tempMap_file,geotec_location)
    postGeoMediaTweet(text,geotec_location[0],geotec_location[1],tempMap)

