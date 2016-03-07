import shutil
import urllib2

from key import GoogleKeyProvider as ggl

gStreetViewKey = ggl.getGoogleStreetViewKey()
baseurl = 'https://maps.googleapis.com/maps/api/streetview?size=%s&location=%f,%f&heading=%f&pitch=%f&key=%s'
scHeading = 90
scPitch = 1.1
scSize = '650x270'
coordinates = []


def getScene(name, center):
	url = baseurl % (scSize,center[0],center[1],scHeading,scPitch,gStreetViewKey)
	img = urllib2.urlopen(url)
	with open(name,'wb') as local_file:
		shutil.copyfileobj(img,local_file)
	return img



if __name__ == "__main__":
	coordinates.append(39.9936197)
	coordinates.append(-0.072568)

	getScene('scfile.png',coordinates)