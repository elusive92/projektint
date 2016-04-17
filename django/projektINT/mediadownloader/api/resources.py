from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication

from mediadownloader.models import Media_request

from tastypie.authorization import DjangoAuthorization
class MediaRequestResource(ModelResource):
    class Meta:
        queryset = Media_request.objects.all()
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        