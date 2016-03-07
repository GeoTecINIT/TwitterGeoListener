#this is a reference File
#To use this file fill the following authentication variables and
#remove the '_' character from folder name, 'key'

googleMapsKey = 'Your_google_maps_key'
googleStreetViewKey = 'Your_google_street_view_key'

def getGoogleMapsKey():
    return googleMapsKey

def getGoogleStreetViewKey():
    return googleStreetViewKey

if __name__ == "__main__":
    print("Your Google Keys are here")