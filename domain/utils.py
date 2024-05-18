from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def sendInfo(data):
    channel_layer = get_channel_layer()

    res = async_to_sync(channel_layer.group_send)(
        "ava",
        {"type": "chat_message", "message": data},
    )
