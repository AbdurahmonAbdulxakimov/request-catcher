from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/(?P<domain>\w+)/$", consumers.DomainConsumer.as_asgi()),
]
