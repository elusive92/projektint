import json
from twitterDownloadApp import twitterDownloadApp
from flickrDownloadApp import flickrDownloadApp

class downloaderAppFactory(object):
    def __init__(self):
        return

    def createApp(self, message):    
        appName = str(message["MediaApp"]["application"])

        if appName == "twitter":
            print("Creating a twitter app")
            return twitterDownloadApp(str(message["MediaApp"]["requestID"]), str(message["MediaApp"]["city"]))  

        if appName == "flickr":
            print("Creating a flickr app")
            return flickrDownloadApp(str(message["MediaApp"]["requestID"]), str(message["MediaApp"]["city"]))   
