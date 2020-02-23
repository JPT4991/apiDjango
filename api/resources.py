from tastypie.resources import ModelResource
from api.models import Post, User
from tastypie.authorization import Authorization

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'

        authorization = Authorization()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

        authorization = Authorization()
        