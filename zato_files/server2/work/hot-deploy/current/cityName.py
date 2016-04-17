#import requests
#from requests_oauthlib import OAuth1

def getCityCordinates(cityName):
"""
    url = 'http://maps.googleapis.com/maps/api/geocode/json'    
    params = {
        "address" : cityName
    }
    response = requests.get(url, params=params)
    
    lat = 0
    lng = 0
    if response.json()["status"] == "OK" and len(response.json()["results"]) > 0:
        lat = response.json()["results"][0]["geometry"]["location"]["lat"]
        lng = response.json()["results"][0]["geometry"]["location"]["lng"]
    return {"lat": lat, "lng": lng}
"""