from downloaderApp import downloaderApp
from dataType import aplicationType
import requests
from requests_oauthlib import OAuth1
#from requests_oauthlib import oauth1_auth
import json
from cityName import getCityCordinates

class twitterDownloadApp(downloaderApp):
    __requestID = None
    __payload = None
    __city = None
    
    def __init__(self, requestID, city):
        self.__requestID = requestID
        self.__city = city
        return

    def get_requestID(self):
        return self.__requestID
    
    def set_payload(self, data):
        self.__payload = data
        
    def get_payload(self):
        return self.__payload

    def get_city(self):
        return self.__city

    def get_ID(self):
        return aplicationType.twitter
 
    def get_clean_payload(self):
        jsonAttList = []

        type(self.__payload)
        for i in range(len(self.__payload.json()['statuses'])):
#            jsonData = {
#                "application" : "twitter",
#                "text" : self.__payload.json()['statuses'][i]['text']
#            }
#            jsonAttList.append(jsonData)
	    jsonAttList.append(self.__payload.json()['statuses'][i]['text'])
	dict = {'TwitterApp' : {'status': '1', 'requestID': self.__requestID, 'fields': jsonAttList} };	
	return json.dumps(dict)

    def do(self):
        oauth_token_secret = 'FNiTAS06WRHgSKj7HEqPIByr2erFFW5xMd8tsUxMmGtM9'
        oauth_token = '711537152534904832-4KlI3J1XFrqdXrZbP7vfffOQszrOe8X'
        csecret = 'wEn2B4U5vVXaMBBclHlTZ1wTo9M5I0kIAvumMhMTAoM0SiRWYL'
        ckey = 'Twe2KtndSTGctRk2XfglWdrn0'
        auth = OAuth1(ckey, csecret, oauth_token, oauth_token_secret)

        cordinates = getCityCordinates(self.__city)
	url = "https://api.twitter.com/1.1/search/tweets.json"

        params = {
            "q" : "*",
            "geocode" : "{lat},{lng},{range}mi".format(lat=cordinates['lat'], lng=cordinates['lng'], range='10')
        }
	self.__payload = requests.get(url, auth=auth, params=params)
	return
	