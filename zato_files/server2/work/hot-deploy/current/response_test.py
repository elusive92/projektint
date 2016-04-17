# Zato
from zato.server.service import Service

class GetClientDetails(Service):
	def handle(self):
		self.response.payload = self.request.payload
