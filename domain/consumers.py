import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer


class DomainConsumer(WebsocketConsumer):
    def connect(self):
        self.subdomain = self.scope["url_route"]["kwargs"]["subdomain"]
        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.subdomain, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.subdomain, self.channel_name)

    # Receive message from room group
    def request_info(self, event):
        data = event["data"]
        # Send data to WebSocket
        self.send(text_data=json.dumps({"data": data}))
