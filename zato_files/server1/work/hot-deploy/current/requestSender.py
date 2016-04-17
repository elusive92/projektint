import json
import time
import sys
import requests
from zato.server.service import Service

class GetClientDetails(Service):
	def handle(self):
#		test22 = 
#		request = json.loads(self.request.payload)
#		requestID = request.json()["requestID"]
#		fields = request.json()["fields"]
#
#		headers = {
#		    'Content-Type': 'application/json',
#		}
#
#		data = '{"requestID": "10", "app_type": "Twitter", "payload": "another-post22"}'
#
#		requests.post('http://localhost:8000/api/v1/mediarequest/?username=admin&api_key=65714eec974d6ac96f6f3d6dce2f8050fe250ecf', headers=headers, data=data)
		url = 'http://192.168.0.105:8000/api/v1/mediarequest/?username=admin&api_key=65714eec974d6ac96f6f3d6dce2f8050fe250ecf'
	
		appName = list(self.request.payload)[0]
		for i in self.request.payload[appName]['fields']:
			payload = {"requestID": "0", "app_type": appName, "payload": i}
			headers = {'content-type': 'application/json'}
			json_data = json.dumps(payload)
			r = requests.post(url, data=json.dumps(payload), headers=headers)