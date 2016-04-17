from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MainViewController(models.Model):
    name = models.CharField(default="None",max_length=120)
    description =  models.TextField(default="Standard description")

    def __unicode__(self):
        return unicode(self.name)
    