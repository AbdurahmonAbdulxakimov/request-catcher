from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_to_ws(subdomain, data):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        subdomain,
        {"type": "request_info", "data": data},
    )


def send_info(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        request = args[1]

        # Subdomain
        subdomain = request.META.get("HTTP_HOST").split(".")[0]
        method = request.method
        headers = request.headers
        path = kwargs.pop("path", "/")

        # Combine data
        request_data = {
            "method": method,
            "headers": dict(headers),
            "path": path,
            "data": dict(request.data),
        }

        # if requested "favicon" then do nothing
        if path == "favicon.ico":
            return

        # Send data to WebSocket
        send_to_ws(subdomain, request_data)

        return func(*args, **kwargs)

    return wrapper
