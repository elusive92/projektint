import json
import time
import sys
from zato.server.service import Service
#import downloaderApp
from downloaderAppFactory import downloaderAppFactory
#import cityName
#import dataType
#import twitterDownloadApp
import requests

class GetClientDetails(Service):
	def handle(self):
		AppFactory = downloaderAppFactory()
		app = AppFactory.createApp(self.request.payload)
		app.do()
		requests.post('http://localhost:11223/request-sender', data=str(app.get_clean_payload()))
#		self.response.payload = 'OK'

