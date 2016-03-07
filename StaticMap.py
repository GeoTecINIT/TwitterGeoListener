import shutil
import urllib2

from key import GoogleKeyProvider as ggl

#static maps
gmapsKey = ggl.getGoogleMapsKey()
baseurl = 'https://maps.googleapis.com/maps/api/staticmap?maptype=%s&center=%f,%f&zoom=%i&size=%s&key=%s'
baseurl_style = 'https://maps.googleapis.com/maps/api/staticmap?center=%f,%f&zoom=%i&size=%s&style=%skey=%s'
mapType = 'satellite'
mapSize = '320x200'
styleArray = ['element:labels|visibility:on',
 'element:geometry.stroke|visibility:off', 
 'feature:landscape|element:geometry|saturation:-100', 
 'feature:water|saturation:-100|invert_lightness:true',
 'feature:road|visibility:off',
 'markers=size:small|%f,%f']
style = ''

for s in styleArray:
	style = style + s + '&'

coordinates = []


def getMap(name, center,zoom):
	url = baseurl % (mapType,center[0],center[1],zoom,mapSize,gmapsKey)
	img = urllib2.urlopen(url)
	with open(name,'wb') as local_file:
		shutil.copyfileobj(img,local_file)
	return img

def getStyledMap(name, center, zoom):
	url = baseurl_style % (center[0],center[1],zoom,mapSize,(style%(center[0],center[1])),gmapsKey)
	print url
	img = urllib2.urlopen(url)
	with open(name,'wb') as local_file:
		shutil.copyfileobj(img,local_file)
	return img


if __name__ == "__main__":
	coordinates.append(39.9936197)
	coordinates.append(-0.072568)

	getStyledMap('mapfile.png',coordinates, 14)