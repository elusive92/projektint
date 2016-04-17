import json
import time
import sys
from zato.server.service import Service
import downloaderApp
#import downloaderAppFactory
import cityName
import dataType
#import twitterDownloadApp

class GetClientDetails(Service):
    def handle(self):
        self.response.payload = self.request.payload

