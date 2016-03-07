

def getPlaceCentroid(place):
	bbox = place['bounding_box']
	coord = bbox['coordinates']
	center = [] 
	a = 0.0
	b = 0.0
	for i in coord:
		for j in i:
			a = a + j[0]
			b = b + j[1]
	center.append(a/4.0)
	center.append(b/4.0)
	return center


if __name__ == "__main__":
	print('You have your Tweet Place')