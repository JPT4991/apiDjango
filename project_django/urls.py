from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path
from api.resources import PostResource, UserResource

post_resource = PostResource()
user_resource = UserResource()


urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include(post_resource.urls)),
    url('api/', include(user_resource.urls)),
]
