from django.urls import re_path

from domain.consumers import DomainConsumer

websocket_urlpatterns = [
    re_path(r"ws/(?P<subdomain>\w+)/$", DomainConsumer.as_asgi()),
]
