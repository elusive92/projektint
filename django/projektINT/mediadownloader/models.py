from django.db import models

# Create your models here.
class Media_request_manager(models.Manager):
    def get_payload(self, appID, app_name):
        return super(Media_request_manager, self).filter(requestID=appID, app_type=app_name)

class Media_request(models.Model):
    requestID = models.CharField(max_length=500)
    app_type = models.CharField(max_length=120)
    payload = models.CharField(max_length=240)
    
    objects = Media_request_manager()
    items = Media_request_manager()
    
    def __unicode__(self):
        return self.requestID
