from django.contrib import admin

# Register your models here.
from mediadownloader.models import Media_request

class Media_request_admin(admin.ModelAdmin):
    class Meta:
        model = Media_request
        
admin.site.register(Media_request, Media_request_admin)